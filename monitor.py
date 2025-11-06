import asyncio
import os
import re
from datetime import datetime, timedelta
from typing import Set, Dict
from aiogram import Bot
from config import ADMIN_IDS


class XrayMonitor:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.last_positions: Dict[str, int] = {}
        self.known_ips: Set[str] = set()
        self.log_files = [
            '/etc/v2ray-agent/xray/access.log',
            '/var/log/xray/access.log',
            '/usr/local/etc/xray/access.log'
        ]

    async def start_monitoring(self):
        """Запускает мониторинг журналов Xray"""
        while True:
            try:
                await self.check_logs()
                await asyncio.sleep(60)  # Проверка каждую минуту
            except Exception as e:
                print(f"Ошибка мониторинга: {e}")
                await asyncio.sleep(60)

    async def check_logs(self):
        """Проверяет журналы на новые подключения"""
        current_time = datetime.now()
        new_ips = set()

        for log_file in self.log_files:
            ips = await self.parse_log_file(log_file, current_time)
            new_ips.update(ips)

        # Фильтруем только новые IP
        truly_new_ips = new_ips - self.known_ips

        if truly_new_ips:
            self.known_ips.update(truly_new_ips)
            await self.send_notification(truly_new_ips, current_time)

    async def parse_log_file(self, log_file: str, current_time: datetime) -> Set[str]:
        """Парсит файл лога и возвращает новые IP"""
        ips = set()

        try:
            # Получаем текущую позицию в файле
            current_position = self.last_positions.get(log_file, 0)

            try:
                with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                    # Перемещаемся к последней известной позиции
                    if current_position > 0:
                        f.seek(current_position)

                    # Читаем новые строки
                    new_lines = f.readlines()

                    # Сохраняем новую позицию
                    self.last_positions[log_file] = f.tell()

                    # Парсим IP из новых строк
                    for line in new_lines:
                        ip = self.extract_ip_from_line(line, current_time)
                        if ip:
                            ips.add(ip)

            except FileNotFoundError:
                print(f"Файл лога не найден: {log_file}")
            except UnicodeDecodeError:
                # Пробуем с другой кодировкой
                with open(log_file, 'r', encoding='latin-1', errors='ignore') as f:
                    if current_position > 0:
                        f.seek(current_position)

                    new_lines = f.readlines()
                    self.last_positions[log_file] = f.tell()

                    for line in new_lines:
                        ip = self.extract_ip_from_line(line, current_time)
                        if ip:
                            ips.add(ip)

        except Exception as e:
            print(f"Ошибка чтения файла {log_file}: {e}")

        return ips

    def extract_ip_from_line(self, line: str, current_time: datetime) -> str:
        """Извлекает IP из строки лога и проверяет время"""
        try:
            # Пропускаем пустые строки
            if not line.strip():
                return None

            # Парсим время из лога (формат: 2025/11/06 10:16:50.792079)
            time_match = re.match(r'(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})', line)
            if not time_match:
                return None

            log_time_str = time_match.group(1)
            log_time = datetime.strptime(log_time_str, '%Y/%m/%d %H:%M:%S')

            # Проверяем, что запись не старше 2 минут
            if current_time - log_time > timedelta(minutes=2):
                return None

            # Ищем IP адрес в строке
            ip_pattern = r'from (\d+\.\d+\.\d+\.\d+):\d+'
            ip_match = re.search(ip_pattern, line)

            if ip_match:
                ip = ip_match.group(1)

                # Игнорируем локальные и служебные IP
                if not self.is_private_ip(ip):
                    return ip

        except Exception as e:
            print(f"Ошибка парсинга строки: {e}")

        return None

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
            "🔍 **Новые подключения к VPN**\n"
            f"*Время:* {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"*Количество IP:* {len(new_ips)}\n"
            f"*IP адреса:*\n"
        )

        for ip in sorted(new_ips):
            message += f"• `{ip}`\n"

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
            f"📊 **Статистика мониторинга**\n"
            f"*Отслеживаемых IP:* {len(self.known_ips)}\n"
            f"*Файлы логов:* {len([f for f in self.log_files if os.path.exists(f)])}\n"
            f"*Последняя проверка:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
