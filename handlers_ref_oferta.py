from aiogram import Router, types
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import URL_BOT, LANG
from keyboards import ref_kb, offer_kb
from lexicon import lexicon

router = Router()


@router.callback_query(lambda c: c.data == "invite")
async def invite_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['ref'],
        reply_markup=ref_kb()
    )


@router.callback_query(lambda c: c.data == "offer")
async def offer_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        lexicon[LANG]['offer'],
        reply_markup=offer_kb()
    )