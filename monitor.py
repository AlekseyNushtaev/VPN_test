import asyncio
import re
from datetime import datetime, timedelta
from typing import Set, Dict
from aiogram import Bot

from config import ADMIN_IDS


class XrayMonitor:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.known_ips: Set[str] = set()
        self.last_check_time = datetime.now()

    async def start_monitoring(self):
        """Запускает мониторинг журналов Xray через journalctl"""
        while True:
            try:
                await self.check_journalctl_logs()
                await asyncio.sleep(60)  # Проверка каждую минуту
            except Exception as e:
                print(f"Ошибка мониторинга: {e}")
                await asyncio.sleep(60)

    async def check_journalctl_logs(self):
        """Проверяет логи Xray через journalctl за последнюю минуту"""
        current_time = datetime.now()
        new_ips = set()

        try:
            # Получаем логи за последнюю минуту
            since_time = (current_time - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

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

        # Фильтруем только новые IP
        truly_new_ips = new_ips - self.known_ips

        if truly_new_ips:
            self.known_ips.update(truly_new_ips)
            await self.send_notification(truly_new_ips, current_time)

        self.last_check_time = current_time

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
            # Пример строки: "from 92.255.142.115:45159 accepted tcp:clients4.google.com:443"
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

    async def send_notification(self, new_ips: Set[str], timestamp: datetime):
        """Отправляет уведомление админам о новых подключениях"""
        if not new_ips or not ADMIN_IDS:
            return

        message = (
            "🔍 **Новые подключения к VPN (через journalctl)**\n"
            f"*Время:* {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"*Количество IP:* {len(new_ips)}\n"
            f"*IP адреса:*\n"
        )

        for ip in sorted(new_ips):
            # Попробуем получить информацию о стране (опционально)
            message += f"• `{ip}` \n"

        for admin_id in ADMIN_IDS:
            try:
                await self.bot.send_message(
                    admin_id,
                    message,
                    parse_mode='Markdown'
                )
            except Exception as e:
                print(f"Не удалось отправить сообщение админу {admin_id}: {e}")


    async def get_current_stats(self) -> str:
        """Возвращает текущую статистику мониторинга"""
        return (
            f"📊 **Статистика мониторинга (journalctl)**\n"
            f"*Отслеживаемых IP:* {len(self.known_ips)}\n"
            f"*Последняя проверка:* {self.last_check_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"*Следующая проверка:* {(self.last_check_time + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')}"
        )

    async def get_recent_activity(self, hours: int = 24) -> str:
        """Получает активность за указанный период"""
        try:
            since_time = (datetime.now() - timedelta(hours=hours)).strftime("%Y-%m-%d %H:%M:%S")

            process = await asyncio.create_subprocess_shell(
                f"journalctl -u xray --since '{since_time}' --no-pager",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                logs = stdout.decode('utf-8', errors='ignore')
                ips = self.parse_journalctl_logs(logs)

                return (
                    f"📈 **Активность за {hours}ч**\n"
                    f"*Уникальных IP:* {len(ips)}\n"
                    f"*Всего записей в логе:* {len(logs.splitlines())}\n"
                    f"*Период:* {since_time} - сейчас"
                )
            else:
                return "❌ Не удалось получить данные о активности"

        except Exception as e:
            return f"❌ Ошибка получения активности: {str(e)}"
