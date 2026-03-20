from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import (
    main_menu_kb,
    back_to_menu_kb,
    back_to_menu_and_contacts_kb,
    about_kb,
    back_to_about_kb,
    back_to_about_and_contacts_kb,
    contacts_kb,
)
from texts import (
    START_TEXT,
    ABOUT_TEXT,
    COLORING_TEXT,
    CUTS_TEXT,
    TREATMENT_TEXT,
    CONTACTS_TEXT,
    SHAMPOO_TEXT,
    CONDITIONER_TEXT,
    MASK_CARE_TEXT,
    MASK_COLOR_TEXT,
)
from utils import replace_with_photo_section, replace_with_text_section, photo

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(
        photo("main.jpeg"), caption=START_TEXT, reply_markup=main_menu_kb()
    )


@router.callback_query(F.data == "menu")
async def menu(call: CallbackQuery):
    await replace_with_photo_section(
        call, START_TEXT, "main.jpeg", main_menu_kb()
    )
    await call.answer()


@router.callback_query(F.data == "about")
async def about(call: CallbackQuery):
    await replace_with_photo_section(call, ABOUT_TEXT, "about.jpeg", about_kb())
    await call.answer()


@router.callback_query(F.data == "coloring")
async def coloring(call: CallbackQuery):
    await replace_with_text_section(call, COLORING_TEXT, back_to_menu_and_contacts_kb())
    await call.answer()


@router.callback_query(F.data == "cuts")
async def cuts(call: CallbackQuery):
    await replace_with_text_section(call, CUTS_TEXT, back_to_menu_and_contacts_kb())
    await call.answer()


@router.callback_query(F.data == "treatment")
async def treatment(call: CallbackQuery):
    await replace_with_text_section(call, TREATMENT_TEXT, back_to_menu_and_contacts_kb())
    await call.answer()


@router.callback_query(F.data == "contacts")
async def contacts(call: CallbackQuery):
    await replace_with_text_section(call, CONTACTS_TEXT, contacts_kb())
    await call.answer()


@router.callback_query(F.data == "about_shampoo")
async def about_shampoo(call: CallbackQuery):
    await replace_with_photo_section(
        call, SHAMPOO_TEXT, "shampoo.jpeg", back_to_about_and_contacts_kb()
    )
    await call.answer()


@router.callback_query(F.data == "about_conditioner")
async def about_conditioner(call: CallbackQuery):
    await replace_with_photo_section(
        call, CONDITIONER_TEXT, "conditioner.jpeg", back_to_about_and_contacts_kb()
    )
    await call.answer()


@router.callback_query(F.data == "about_mask_care")
async def about_mask_care(call: CallbackQuery):
    await replace_with_photo_section(
        call, MASK_CARE_TEXT, "mask_care.jpeg", back_to_about_and_contacts_kb()
    )
    await call.answer()


@router.callback_query(F.data == "about_mask_color")
async def about_mask_color(call: CallbackQuery):
    await replace_with_photo_section(
        call, MASK_COLOR_TEXT, "mask_color.jpeg", back_to_about_and_contacts_kb()
    )
    await call.answer()
