from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1️⃣ Обо мне и моём бренде", callback_data="about"
                )
            ],
            [InlineKeyboardButton(text="2️⃣ Окрашивание", callback_data="coloring")],
            [InlineKeyboardButton(text="3️⃣ Стрижки и укладки", callback_data="cuts")],
            [InlineKeyboardButton(text="4️⃣ Лечение волос", callback_data="treatment")],
            [
                InlineKeyboardButton(
                    text="5️⃣ Записаться / Контакты", callback_data="contacts"
                )
            ],
        ]
    )


def back_to_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="menu")]
        ]
    )


def back_to_menu_and_contacts_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="5️⃣ Записаться / Контакты", callback_data="contacts"
                )
            ],
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="menu")],
        ]
    )


def about_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🧴 Шампуни", callback_data="about_shampoo")],
            [
                InlineKeyboardButton(
                    text="💧 Кондиционеры", callback_data="about_conditioner"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💜 Маска «уход»", callback_data="about_mask_care"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💜 Маска «цвет»", callback_data="about_mask_color"
                )
            ],
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="menu")],
        ]
    )


def back_to_about_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔙 Назад в раздел «Обо мне»", callback_data="about"
                )
            ]
        ]
    )


def back_to_about_and_contacts_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="5️⃣ Записаться / Контакты", callback_data="contacts"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔙 Назад в раздел «Обо мне»", callback_data="about"
                )
            ],
        ]
    )


def contacts_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📩 Написать в Telegram", url="https://t.me/tatyana_lilu"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💬 Написать в WhatsApp", url="https://wa.me/79531561771"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗓 Записаться онлайн", url="https://dikidi.ru/1475778"
                )
            ],
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="menu")],
        ]
    )
