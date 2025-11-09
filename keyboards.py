from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import LANG, URL_BOT
from lexicon import lexicon


def main_menu_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['connect'], callback_data="connect")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['friends'], callback_data="invite")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help'], callback_data="help")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['offer'], callback_data="offer")]
        ]
    )


def devices_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_android'], callback_data="android")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_ios'], callback_data="ios")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_windows'], callback_data="windows")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_macos'], callback_data="macos")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def android_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_app'], url="https://play.google.com/store/apps/details?id=com.happproxy&hl=en&pli=1")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_connect'], callback_data="connect_phone")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="connect")]
        ]
    )


def ios_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_app'], url="https://apps.apple.com/ru/app/happ-proxy-utility-plus/id6746188973")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_connect'], callback_data="connect_phone")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="connect")]
        ]
    )


def windows_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_app'], url="https://github.com/Happ-proxy/happ-desktop/releases/latest/download/setup-Happ.x86.exe")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_connect'], callback_data="connect_comp")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="connect")]
        ]
    )


def macos_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_app'], url="https://apps.apple.com/ru/app/happ-proxy-utility-plus/id6746188973")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['get_connect'], callback_data="connect_comp")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="connect")]
        ]
    )


def end_connect_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu_del")]
        ]
    )


def ref_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['share'], url=f"tg://msg_url?url={URL_BOT}")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def offer_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['offer'], url="https://winvpn.org/oferta/")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['politic'], url="https://winvpn.org/privacy_mobile_app/")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['politic_back'], url="https://winvpn.org/refund/")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")],
        ]
    )


def help_main_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_android'], callback_data="help_android")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_ios'], callback_data="help_ios")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_windows'], callback_data="help_windows")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['help_macos'], callback_data="help_macos")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_android_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['invalid_key'], callback_data="help_android_invalid_key")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['slow_vpn'], callback_data="help_android_slow_vpn")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['auto_disconnect'], callback_data="help_android_auto_disconnect")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['tiktok_not_working'], callback_data="help_android_tiktok_not_working")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['mobile_network'], callback_data="help_android_mobile_network")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['cant_install'], callback_data="help_android_cant_install")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['config_error'], callback_data="help_android_config_error")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['friend_days'], callback_data="help_android_friend_days")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_back")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_back_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_android")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_ios_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['slow_vpn'], callback_data="help_ios_slow_vpn")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['auto_disconnect'], callback_data="help_ios_auto_disconnect")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['tiktok_not_working'], callback_data="help_ios_tiktok_not_working")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['mobile_network'], callback_data="help_ios_mobile_network")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['cant_install'], callback_data="help_ios_cant_install")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['config_error'], callback_data="help_ios_config_error")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['friend_days'], callback_data="help_ios_friend_days")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_back")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_ios_back_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_ios")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_macos_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['slow_vpn'], callback_data="help_macos_slow_vpn")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['auto_disconnect'], callback_data="help_macos_auto_disconnect")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['cant_install'], callback_data="help_macos_cant_install")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['config_error'], callback_data="help_macos_config_error")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['friend_days'], callback_data="help_macos_friend_days")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_back")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_macos_back_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_macos")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_windows_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['windows_browser'], callback_data="help_windows_browser")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['windows_telegram'], callback_data="help_windows_telegram")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['windows_internet'], callback_data="help_windows_internet")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_back")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )


def help_windows_back_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['back'], callback_data="help_windows")],
            [InlineKeyboardButton(text=lexicon[LANG]['buttons']['main_menu'], callback_data="main_menu")]
        ]
    )
