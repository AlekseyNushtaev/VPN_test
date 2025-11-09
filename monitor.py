import asyncio
import re
from datetime import datetime, timedelta
from typing import Set
from aiogram import Bot
from sqlalchemy import select

from db.models import Session, Connection


class XrayMonitor:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.known_ips: Set[str] = set()
        self.last_check_time = datetime.now()

    async def load_existing_ips(self):
        """Загружает существующие IP из базы данных при старте"""
        try:
            async with Session() as session:
                result = await session.execute(select(Connection.ip))
                existing_ips = result.scalars().all()
                self.known_ips.update(existing_ips)
                print(f"Загружено {len(existing_ips)} существующих IP из БД")
        except Exception as e:
            print(f"Ошибка загрузки IP из БД: {e}")

    async def start_monitoring(self):
        """Запускает мониторинг журналов Xray через journalctl"""
        # Загружаем существующие IP при старте
        await self.load_existing_ips()

        while True:
            try:
                await self.check_journalctl_logs()
                await asyncio.sleep(300)  # Проверка каждые 5 минут (300 секунд)
            except Exception as e:
                print(f"Ошибка мониторинга: {e}")
                await asyncio.sleep(300)

    async def check_journalctl_logs(self):
        """Проверяет логи Xray через journalctl за последние 5 минут"""
        current_time = datetime.now()
        new_ips = set()

        try:
            # Получаем логи за последние 5 минут
            since_time = (current_time - timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")

            # Запускаем процесс journalctl
            process = await asyncio.create_subprocess_shell(
                f"journalctl -u xray --since '{since_time}' --no-pager",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                logs = stdout.decode('utf-8', errors='ignore')
                new_ips = self.parse_journalctl_logs(logs)
            else:
                error_msg = stderr.decode('utf-8', errors='ignore')
                print(f"Ошибка journalctl: {error_msg}")

                # Пробуем альтернативный вариант (может потребоваться sudo)
                process = await asyncio.create_subprocess_shell(
                    f"sudo journalctl -u xray --since '{since_time}' --no-pager",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                stdout, stderr = await process.communicate()
                if process.returncode == 0:
                    logs = stdout.decode('utf-8', errors='ignore')
                    new_ips = self.parse_journalctl_logs(logs)

        except Exception as e:
            print(f"Ошибка выполнения journalctl: {e}")

        # Фильтруем только новые IP (которых нет в known_ips)
        truly_new_ips = new_ips - self.known_ips

        if truly_new_ips:
            # Сохраняем только действительно новые IP в БД
            saved_count = await self.save_new_connections(truly_new_ips, current_time)
            if saved_count > 0:
                self.known_ips.update(truly_new_ips)
                print(f"Сохранено {saved_count} новых IP в БД")

        # Отправляем статистику за 5 минут
        await self.send_5min_stats(len(new_ips), current_time)

        self.last_check_time = current_time

    async def save_new_connections(self, new_ips: Set[str], timestamp: datetime) -> int:
        """Сохраняет новые подключения в базу данных и возвращает количество сохраненных"""
        saved_count = 0
        try:
            async with Session() as session:
                for ip in new_ips:
                    try:
                        # Проверяем, нет ли уже такого IP в БД (дополнительная проверка)
                        existing = await session.execute(
                            select(Connection).where(Connection.ip == ip)
                        )
                        if existing.scalar_one_or_none() is None:
                            connection = Connection(
                                ip=ip,
                                start_time=timestamp
                            )
                            session.add(connection)
                            saved_count += 1
                    except Exception as e:
                        print(f"Ошибка при проверке IP {ip}: {e}")
                        continue

                await session.commit()
                return saved_count

        except Exception as e:
            print(f"Ошибка сохранения подключений в БД: {e}")
            return 0

    async def send_5min_stats(self, unique_ips_count: int, timestamp: datetime):
        """Отправляет статистику за 5 минут в Telegram"""
        try:
            message = (
                f"📊 **Статистика подключений за 5 минут**\n"
                f"*Время:* {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"*Уникальных IP:* {unique_ips_count}\n"
                f"*Период:* 5 минут"
            )

            await self.bot.send_message(
                1012882762,
                message,
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"Не удалось отправить статистику: {e}")


    def parse_journalctl_logs(self, logs: str) -> Set[str]:
        """Парсит логи journalctl и возвращает IP адреса"""
        ips = set()

        if not logs.strip():
            return ips

        lines = logs.split('\n')

        for line in lines:
            if not line.strip():
                continue

            # Ищем IP адреса в строках с подключениями
            ip = self.extract_ip_from_journal_line(line)
            if ip:
                ips.add(ip)

        return ips

    def extract_ip_from_journal_line(self, line: str) -> str:
        """Извлекает IP адрес из строки journalctl"""
        try:
            # Пропускаем системные строки journalctl
            if line.startswith('--') or 'Logs begin' in line or 'Logs end' in line:
                return None

            # Ищем паттерны IP адресов в логах Xray
            ip_patterns = [
                r'from\s+(\d+\.\d+\.\d+\.\d+):\d+',  # from IP:PORT
                r'(\d+\.\d+\.\d+\.\d+):\d+\s+accepted',  # IP:PORT accepted
                r'client:\s+(\d+\.\d+\.\d+\.\d+)',  # client: IP
            ]

            for pattern in ip_patterns:
                match = re.search(pattern, line)
                if match:
                    ip = match.group(1)

                    # Проверяем, что IP валидный и не приватный
                    if self.is_valid_ip(ip) and not self.is_private_ip(ip):
                        return ip

        except Exception as e:
            print(f"Ошибка парсинга строки journalctl: {e}")

        return None

    def is_valid_ip(self, ip: str) -> bool:
        """Проверяет валидность IP адреса"""
        ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(ip_pattern, ip):
            return False

        # Проверяем, что каждый октет в диапазоне 0-255
        octets = ip.split('.')
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False

        return True

    def is_private_ip(self, ip: str) -> bool:
        """Проверяет, является ли IP приватным"""
        private_ranges = [
            '10.', '192.168.', '172.16.', '172.17.', '172.18.', '172.19.',
            '172.20.', '172.21.', '172.22.', '172.23.', '172.24.', '172.25.',
            '172.26.', '172.27.', '172.28.', '172.29.', '172.30.', '172.31.',
            '127.', '169.254.', '::1'
        ]

        return any(ip.startswith(prefix) for prefix in private_ranges)
