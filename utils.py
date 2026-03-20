from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, FSInputFile

from config import IMAGES_DIR


def photo(filename: str) -> FSInputFile:
    return FSInputFile(IMAGES_DIR / filename)


async def safe_delete_message(call: CallbackQuery) -> None:
    with suppress(TelegramBadRequest):
        if call.message is None:
            return
        await call.message.delete()


async def replace_with_photo_section(
    call: CallbackQuery, text: str, image_path: str, reply_markup: InlineKeyboardMarkup
):
    if call.message is None:
        return
    await safe_delete_message(call)
    await call.message.answer_photo(
        photo(image_path), caption=text, reply_markup=reply_markup
    )


async def replace_with_text_section(
    call: CallbackQuery, text: str, reply_markup: InlineKeyboardMarkup
):
    if call.message is None:
        return
    await safe_delete_message(call)
    await call.message.answer(text, reply_markup=reply_markup)
