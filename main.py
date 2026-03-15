import os
import asyncio
from pathlib import Path
from contextlib import suppress
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile,
)
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "images"

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


START_TEXT = (
    "Здравствуйте! Меня зовут Татьяна.\n\n"
    "Я рада приветствовать вас в моем профессиональном пространстве.\n\n"
    "💁‍♀️ Я действующий мастер с более чем 15-летним опытом, парикмахер, колорист и тритментолог.\n"
    "Моя специализация — это не просто стрижка, и окрашивание а здоровье волос на молекулярном уровне и сложный цвет в окрашивание.\n"
    "Постоянно учусь, тестирую новинки и применяю только те составы, которые безопасны и эффективны.\n"
    "Разбираю продукты по ингредиентам и создаю свой собственный бренд профессионального ухода.\n"
    "К вашим волосам я подхожу как ученый и как художник.\n\n"
    "📌 Выберите, что вас интересует:"
)

ABOUT_TEXT = (
    "1️⃣ Обо мне и моём бренде\n\n"
    "Всё началось с моей собственной проблемы. У меня очень жирная кожа головы и тонкие волосы, которые требовали мытья буквально через день. "
    "Я перепробовала десятки шампуней: и масс-маркет, и люксовые, и профессиональные бренды. Но каждый из них либо утяжелял волосы, "
    "лишая объёма, либо вызывал раздражение, либо просто не решал проблему.\n\n"
    "Мне хотелось по-настоящему натурального состава, который бережно очищает, не нарушая микробиом кожи головы, "
    "и при этом даёт объём и лёгкость. Тогда я создала шампунь для себя. Итог превзошёл ожидания: волосы перестали жирниться через день, "
    "обрели объём и начали расти быстрее.\n\n"
    "Так родился мой бренд — из любви к себе и желания помочь вам обрести здоровые волосы без компромиссов. 💖\n\n"
    "👇 Выбери, что тебя интересует:"
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
    "🗓 Онлайн-запись: https://dikidi.ru/1475778\n\n"
)

SHAMPOO_TEXT = (
    "🧴 Шампуни\n\n"
    "PRO-WEIGHTLESS COLOR 🫧\n"
    "«Три решения в одной формуле»\n"
    "Его инновационная формула работает у корней и по всей длине.\n\n"
    "Биотехнологичный экстракт клеток оливы пробуждает фолликулы и стимулирует рост более сильных и здоровых волос.\n"
    "Комплекс жидкого шелка и кератина создает невесомую защитную мембрану вокруг каждого волоска, запечатывая цвет внутри.\n\n"
    "• Восстанавливает структуру\n"
    "• Сохраняет цвет и блеск\n"
    "• Снимает статическое электричество\n"
    "• Очищает без утяжеления\n"
    "• Придает упругость и плотность\n"
    "• Подходит для чувствительной кожи головы и тонких волос"
)

CONDITIONER_TEXT = (
    "💧 Кондиционеры\n\n"
    "• КОМПЛЕКС МАСЕЛ (Ши, Миндальное, Жожоба) И ПРОТЕИНОВ\n"
    "Восстанавливают липидный баланс, дают сияние без утяжеления.\n\n"
    "Кондиционер KERATIN CHARGE ⚡\n"
    "Молекулярная формула кератина и шелка. Интенсивная терапия для сильно поврежденных волос.\n\n"
    "Как работает состав:\n"
    "· Глубокое восстановление изнутри: низкомолекулярный кератин и аминокислоты заполняют микроповреждения.\n"
    "· Мгновенная гладкость и блеск: комплекс протеинов и шелка создает легкую smoothing-пленку.\n"
    "· Технология 18-MEA: воссоздает естественный защитный барьер и дает термозащиту.\n"
    "· Интенсивное питание и уплотнение: пантенол, масла и керамиды питают волосы по всей длине."
)

MASK_CARE_TEXT = (
    "💜 Маска «уход»\n\n"
    "COLOR THERAPY\n"
    "Комплексное молекулярное восстановление.\n"
    "Интенсивный уход для ослабленных волос.\n\n"
    "Глубинное восстановление и уплотнение волос.\n"
    "Элая Ренова в паре с 3 видами кератина «цементирует» микротрещины и уплотняет волокно.\n\n"
    "Молекулярная формула:\n"
    "• Элая Ренова (фосфолипиды, церамиды, сфинголипиды)\n"
    "• Мульти-кератиновый комплекс (3 вида)\n"
    "• Аминокислоты шелка + комплекс протеинов\n"
    "• Комплекс питательных масел (жожоба и др.)\n"
    "• Инновационные комплексы (CML Complex, Треалекс)"
)

MASK_COLOR_TEXT = (
    "💜 Маска «цвет»\n\n"
    "VITAL REPAIR\n"
    "Липидно-протеиновая маска с защитой цвета и структуры.\n"
    "Формула работает на трех уровнях: защищает пигмент, уплотняет структуру, создает термобарьер.\n\n"
    "Научная формула:\n"
    "• Гидролизованный кератин (низкая молекулярная масса)\n"
    "• 18-MEA комплекс\n"
    "• Комплекс масел (Ши, Миндальное, Жожоба) и протеинов\n\n"
    "📩 Хотите попробовать мои средства или заказать индивидуальный уход?\n"
    "Пишите в личные сообщения: https://t.me/tatyana_lilu\n"
    "+7 953 156 1771 | @tatyana_lilu"
)


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
    await replace_with_text_section(call, COLORING_TEXT, back_to_menu_kb())
    await call.answer()


@router.callback_query(F.data == "cuts")
async def cuts(call: CallbackQuery):
    await replace_with_text_section(call, CUTS_TEXT, back_to_menu_kb())
    await call.answer()


@router.callback_query(F.data == "treatment")
async def treatment(call: CallbackQuery):
    await replace_with_text_section(call, TREATMENT_TEXT, back_to_menu_kb())
    await call.answer()


@router.callback_query(F.data == "contacts")
async def contacts(call: CallbackQuery):
    await replace_with_text_section(call, CONTACTS_TEXT, contacts_kb())
    await call.answer()


@router.callback_query(F.data == "about_shampoo")
async def about_shampoo(call: CallbackQuery):
    await replace_with_text_section(call, SHAMPOO_TEXT, back_to_about_kb())
    await call.answer()


@router.callback_query(F.data == "about_conditioner")
async def about_conditioner(call: CallbackQuery):
    await replace_with_text_section(call, CONDITIONER_TEXT, back_to_about_kb())
    await call.answer()


@router.callback_query(F.data == "about_mask_care")
async def about_mask_care(call: CallbackQuery):
    await replace_with_text_section(call, MASK_CARE_TEXT, back_to_about_kb())
    await call.answer()


@router.callback_query(F.data == "about_mask_color")
async def about_mask_color(call: CallbackQuery):
    await replace_with_text_section(call, MASK_COLOR_TEXT, back_to_about_kb())
    await call.answer()


async def main():
    async with Bot(TOKEN) as bot:
        dp = Dispatcher()
        dp.include_router(router)
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
