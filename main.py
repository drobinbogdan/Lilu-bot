import os
import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

router = Router()


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
            [InlineKeyboardButton(text="🔙 Назад в меню", callback_data="menu")],
        ]
    )


START_TEXT = (
    "Здравствуйте! Меня зовут Татьяна.\n\n"
    "Я рада приветствовать вас в моем профессиональном пространстве.\n\n"
    "💁‍♀️ Я действующий мастер с более чем 15-летним опытом, парикмахер, колорист и тритментолог.\n"
    "Моя специализация — здоровье волос на молекулярном уровне и сложные техники окрашивания.\n\n"
    "📌 Выберите, что вас интересует:"
)

ABOUT_TEXT = (
    "1️⃣ Обо мне и моём бренде\n\n"
    "Я не просто крашу или лечу волосы. Я изучаю составы косметики досконально, разбираю продукты по ингредиентам "
    "и создаю свой собственный бренд профессионального ухода.\n\n"
    "Полный состав каждого средства можно найти в канале ➡️ https://t.me/TF_TERRA_LIVE\n\n"
    "✨ ИНДИВИДУАЛЬНЫЙ ПОДБОР УХОДА\n"
    "Помимо готовых продуктов, я создаю для вас персональный домашний уход: анализирую состояние волос и подбираю компоненты "
    "под вашу задачу.\n\n"
    "📩 Хотите приобрести готовые средства или заказать индивидуальный уход?\n"
    "Пишите мне в личные сообщения — буду рада помочь! 💬"
)

COLORING_TEXT = (
    "2️⃣ Окрашивание (AirTouch, шатуш, total blond)\n\n"
    "🎨 Сложное окрашивание\n"
    "• AirTouch — 💰10000–15000 руб (+ восстанавливающий уход)\n"
    "• Шатуш — 💰8000–12000 руб (+ восстанавливающий уход)\n"
    "• Total Blond — 💰10000–15000 руб (+ восстанавливающий уход)\n\n"
    "Чтобы записаться — откройте раздел «Записаться / Контакты»."
)

CUTS_TEXT = (
    "3️⃣ Стрижки и укладки\n\n"
    "✂️ Стрижка с учётом структуры\n"
    "• Женская — от 1700 руб.\n"
    "• Мужская — от 1200 руб.\n"
    "• Детская (до 12 лет) — от 1000 руб.\n\n"
    "💨 Укладки\n"
    "• Фен/брашинг — от 1800 руб.\n"
    "• Локоны/волны/выпрямление — от 2200 руб.\n"
    "• Вечерние/свадебные — индивидуально\n\n"
    "Чтобы записаться — откройте раздел «Записаться / Контакты»."
)

TREATMENT_TEXT = (
    "4️⃣ Лечение волос / Тритментология\n\n"
    "🧬 Восстановление на молекулярном уровне\n"
    "• Глубокая диагностика — 💰3000 руб.\n"
    "• Экспресс-уход — 💰1200 руб.\n"
    "• Интенсивное восстановление — 💰2000 руб. (курс 3–5 процедур, постоянным гостям скидка 30%)\n\n"
    "Чтобы записаться — откройте раздел «Записаться / Контакты»."
)

CONTACTS_TEXT = (
    "5️⃣ Записаться / Контакты\n\n"
    "📍 Адрес: СПб, ул. Кораблестроителей, 34\n"
    "📞 Телефон: +79531561771\n"
    "📱 Telegram / WhatsApp: @tatyana_lilu\n\n"
    "Для записи напишите мне — и мы подберём удобное время."
)


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(START_TEXT, reply_markup=main_menu_kb())


@router.callback_query(F.data == "menu")
async def menu(call: CallbackQuery):
    await call.message.edit_text(START_TEXT, reply_markup=main_menu_kb())
    await call.answer()


@router.callback_query(F.data == "about")
async def about(call: CallbackQuery):
    await call.message.edit_text(ABOUT_TEXT, reply_markup=back_to_menu_kb())
    await call.answer()


@router.callback_query(F.data == "coloring")
async def coloring(call: CallbackQuery):
    await call.message.edit_text(COLORING_TEXT, reply_markup=back_to_menu_kb())
    await call.answer()


@router.callback_query(F.data == "cuts")
async def cuts(call: CallbackQuery):
    await call.message.edit_text(CUTS_TEXT, reply_markup=back_to_menu_kb())
    await call.answer()


@router.callback_query(F.data == "treatment")
async def treatment(call: CallbackQuery):
    await call.message.edit_text(TREATMENT_TEXT, reply_markup=back_to_menu_kb())
    await call.answer()


@router.callback_query(F.data == "contacts")
async def contacts(call: CallbackQuery):
    await call.message.edit_text(CONTACTS_TEXT, reply_markup=contacts_kb())
    await call.answer()


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
