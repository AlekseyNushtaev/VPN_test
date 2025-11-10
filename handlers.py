from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from sqlalchemy import select, func

from config import LANG
from db.models import User, Session, Connection
from keyboards import main_menu_kb, devices_kb, android_kb, ios_kb, end_connect_kb, windows_kb, \
    macos_kb, admin_reply_kb
from lexicon import lexicon
from config import ADMIN_IDS
import openpyxl
from io import BytesIO
from datetime import datetime

router = Router()


@router.message(Command("stats"))
async def stats_handler(message: types.Message):
    # Проверяем, является ли пользователь администратором
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("У вас нет прав для выполнения этой команды")
        return

    async with Session() as session:
        # Получаем все записи о подключениях
        result = await session.execute(select(Connection))
        connections = result.scalars().all()

    if not connections:
        await message.answer("В базе данных нет записей о подключениях")
        return

    # Создаем новую книгу Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Статистика подключений"

    # Заголовки столбцов
    headers = ["ID", "IP адрес", "Время начала подключения"]
    ws.append(headers)

    # Заполняем данными
    for conn in connections:
        ws.append([
            conn.id,
            conn.ip,
            conn.start_time.strftime("%Y-%m-%d %H:%M:%S")
        ])

    # Авто-ширина столбцов
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column_letter].width = adjusted_width

    # Сохраняем в байтовый поток
    excel_file = BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)

    # Отправляем файл
    filename = f"connections_stats_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.xlsx"
    await message.answer_document(
        types.BufferedInputFile(
            excel_file.read(),
            filename=filename
        ),
        caption="📊 Статистика подключений"
    )

@router.message(Command("start"))
async def start_handler(message: types.Message):
    async with Session() as session:
        result = await session.execute(
            select(User).where(User.user_id == message.from_user.id)
        )
        user = result.scalar_one_or_none()

        if not user:
            user = User(
                user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name
            )
            session.add(user)
            await session.commit()

        await message.answer(
            lexicon[LANG]['start_message'],
            reply_markup=main_menu_kb()
        )

        # Проверка на администратора
        if message.from_user.id in ADMIN_IDS:
            await message.answer(
                "Вы администратор",
                reply_markup=admin_reply_kb()
            )


@router.callback_query(lambda c: c.data == "connect")
async def connect_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['change_connect'],
        reply_markup=devices_kb()
    )


@router.callback_query(lambda c: c.data == "main_menu")
async def main_menu_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['start_message'],
        reply_markup=main_menu_kb()
    )


@router.callback_query(lambda c: c.data == "main_menu_del")
async def main_menu_del_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        lexicon[LANG]['start_message'],
        reply_markup=main_menu_kb()
    )
    try:
        await callback.message.delete()
    except:
        pass


@router.callback_query(lambda c: c.data == "android")
async def android_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(lexicon[LANG]['connect_faq'], reply_markup=android_kb())


@router.callback_query(lambda c: c.data == "ios")
async def ios_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(lexicon[LANG]['connect_faq'], reply_markup=ios_kb())


@router.callback_query(lambda c: c.data == "windows")
async def ios_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(lexicon[LANG]['connect_faq'], reply_markup=windows_kb())


@router.callback_query(lambda c: c.data == "macos")
async def ios_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(lexicon[LANG]['connect_faq'], reply_markup=macos_kb())


@router.callback_query(lambda c: c.data == "connect_phone")
async def connect_phone_handler(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile('phone.bmp'),
        caption=lexicon[LANG]['connect_algoritm'],
        reply_markup=end_connect_kb(),
        parse_mode="Markdown"  # Включаем Markdown для форматирования `URL_VPN`
    )

    # Удаляем предыдущее сообщение с кнопками Android
    try:
        await callback.message.delete()
    except:
        pass


@router.callback_query(lambda c: c.data == "connect_comp")
async def connect_phone_handler(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo=FSInputFile('comp.bmp'),
        caption=lexicon[LANG]['connect_algoritm'],
        reply_markup=end_connect_kb(),
        parse_mode="Markdown"  # Включаем Markdown для форматирования `URL_VPN`
    )

    # Удаляем предыдущее сообщение с кнопками Android
    try:
        await callback.message.delete()
    except:
        pass


@router.message(lambda message: message.text == "📊 Статистика" and message.from_user.id in ADMIN_IDS)
async def admin_stats_message_handler(message: types.Message):
    async with Session() as session:
        users_count = await session.scalar(select(func.count(User.user_id)))
        connections_count = await session.scalar(select(func.count(Connection.id)))

    stats_text = (
        f"📊 Статистика бота:\n\n"
        f"• Зашло в бот - {users_count}\n"
        f"• Выполнило подключений - {connections_count}"
    )

    await message.answer(stats_text)
