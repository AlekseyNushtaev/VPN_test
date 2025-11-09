from aiogram import types, Router

from config import LANG
from keyboards import help_main_kb, help_android_kb, help_back_kb, help_ios_back_kb, help_ios_kb, help_macos_back_kb, \
    help_macos_kb, help_windows_back_kb, help_windows_kb
from lexicon import lexicon

router = Router()


@router.callback_query(lambda c: c.data == "help")
async def help_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['help_main_text'],
        reply_markup=help_main_kb()
    )


@router.callback_query(lambda c: c.data == "help_android")
async def help_android_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['help_android_text'],
        reply_markup=help_android_kb()
    )


@router.callback_query(lambda c: c.data == "help_back")
async def help_back_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['help_main_text'],
        reply_markup=help_main_kb()
    )


# Обработчики для конкретных вопросов Android
@router.callback_query(lambda c: c.data == "help_android_invalid_key")
async def help_android_invalid_key_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['invalid_key_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_android_slow_vpn")
async def help_android_slow_vpn_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['slow_vpn_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_android_auto_disconnect")
async def help_android_auto_disconnect_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['auto_disconnect_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_android_tiktok_not_working")
async def help_android_tiktok_not_working_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['tiktok_not_working_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_android_mobile_network")
async def help_android_mobile_network_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['mobile_network_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_android_cant_install")
async def help_android_cant_install_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['cant_install_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_android_config_error")
async def help_android_config_error_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['config_error_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_android_friend_days")
async def help_android_friend_days_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['friend_days_text'],
        reply_markup=help_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_ios")
async def help_ios_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['help_android_text'],  # Можно использовать тот же текст
        reply_markup=help_ios_kb()
    )


# Обработчики для конкретных вопросов iOS
@router.callback_query(lambda c: c.data == "help_ios_slow_vpn")
async def help_ios_slow_vpn_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['slow_vpn_text'],
        reply_markup=help_ios_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_ios_auto_disconnect")
async def help_ios_auto_disconnect_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['auto_disconnect_text'],
        reply_markup=help_ios_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_ios_tiktok_not_working")
async def help_ios_tiktok_not_working_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['tiktok_not_working_text'],
        reply_markup=help_ios_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_ios_mobile_network")
async def help_ios_mobile_network_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['mobile_network_text'],
        reply_markup=help_ios_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_ios_cant_install")
async def help_ios_cant_install_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['cant_install_text'],
        reply_markup=help_ios_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_ios_config_error")
async def help_ios_config_error_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['config_error_text'],
        reply_markup=help_ios_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_ios_friend_days")
async def help_ios_friend_days_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['friend_days_text'],
        reply_markup=help_ios_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_macos")
async def help_macos_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['help_android_text'],  # Можно использовать тот же текст
        reply_markup=help_macos_kb()
    )


# Обработчики для конкретных вопросов macOS
@router.callback_query(lambda c: c.data == "help_macos_slow_vpn")
async def help_macos_slow_vpn_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['slow_vpn_text'],
        reply_markup=help_macos_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_macos_auto_disconnect")
async def help_macos_auto_disconnect_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['auto_disconnect_text'],
        reply_markup=help_macos_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_macos_cant_install")
async def help_macos_cant_install_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['cant_install_text'],
        reply_markup=help_macos_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_macos_config_error")
async def help_macos_config_error_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['config_error_text'],
        reply_markup=help_macos_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_macos_friend_days")
async def help_macos_friend_days_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['friend_days_text'],
        reply_markup=help_macos_back_kb()
    )


@router.callback_query(lambda c: c.data == "help_windows")
async def help_windows_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['help_windows_text'],
        reply_markup=help_windows_kb()
    )

# Обработчики для конкретных вопросов Windows
@router.callback_query(lambda c: c.data == "help_windows_browser")
async def help_windows_browser_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['windows_browser_issue'],
        reply_markup=help_windows_back_kb()
    )

@router.callback_query(lambda c: c.data == "help_windows_telegram")
async def help_windows_telegram_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['windows_telegram_issue'],
        reply_markup=help_windows_back_kb()
    )

@router.callback_query(lambda c: c.data == "help_windows_internet")
async def help_windows_internet_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['windows_internet_issue'],
        reply_markup=help_windows_back_kb()
    )