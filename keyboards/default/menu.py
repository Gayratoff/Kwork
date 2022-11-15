from aiogram import types
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

from loader import dp,db

menuuz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧑🏻‍💻 Men Frilanserman"),KeyboardButton(text="👤 Men buyurtmachiman")],
        [KeyboardButton(text="💼 Vakasiyalar/Vakansiya joylashtirish")],
        # [KeyboardButton(text='⚙️ Sozlamalar')]

    ],
    resize_keyboard=True
)
@dp.message_handler(text="💼 Vakasiyalar/Vakansiya joylashtirish")
async def bot_start(message: types.Message):
    await message.answer(f"https://t.me/mistruz" , reply_markup=menuuz)
@dp.message_handler(text="🧑🏻‍💻 Men Frilanserman")
async def bot_start(message: types.Message):
    await message.answer(f"<b>🧑🏻‍💻 Men Frilanserman</b>" , reply_markup=frilans)
@dp.message_handler(text="👤 Men buyurtmachiman")
async def bot_start(message: types.Message):
    await message.answer(f"<b>👤 Men buyurtmachiman</b>" , reply_markup=buyurtma)
@dp.message_handler(text="🔝 Asosiy Menyu")
async def bot_start(message: types.Message):
    await message.answer(f"🔝 <b>Asosiy Menyu</b>" , reply_markup=menuuz)


frilans = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📝 Mening  buyurtmalarim"),KeyboardButton(text='📥 Buyurtma olish')],
        [KeyboardButton(text='✅ Mening takliflarim')],
# KeyboardButton(text='🔎 Buyurtmani toping'),
        [KeyboardButton(text='🔝 Asosiy Menyu')]
    ],
    resize_keyboard=True
)

buyurtma=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📝 Mening buyurtmalarim'),KeyboardButton(text='📥 Buyurtma yaratish')],
        [KeyboardButton(text='✅ Freelancer takliflar')],
        [KeyboardButton(text='🔝 Asosiy Menyu')]

    ],
    resize_keyboard=True
)


Buyurtma = ReplyKeyboardMarkup(
    keyboard=[
        # [KeyboardButton(text="Orqaga")],
        [KeyboardButton(text="IT va dasturlash"),KeyboardButton(text='Dizayn')],
        [KeyboardButton(text='SEO va trafik'),KeyboardButton(text='Ijtimoiy tarmoq va reklama')],
        [KeyboardButton(text='Tekstlar va tarjimalar'),KeyboardButton(text='Audio, Video, tasvirga olish')]
    ],
    resize_keyboard=True
)

#-----------------------------------------------------------------------------------------------------

menuru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧑🏻‍💻 Я фрилансер"),KeyboardButton(text="👤 Я заказчик")],
        [KeyboardButton(text="💼 Вакансии/Разместить вакансии")]

    ],
    resize_keyboard=True
)

menuen = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧑🏻‍💻 I am a freelancer"),KeyboardButton(text="👤 I am a customer")],
        [KeyboardButton(text="💼 Jobs/Post Jobs")]

    ],
    resize_keyboard=True
)

#------------------------------------

sozlama = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ismni o'zgartirish"),KeyboardButton(text="Raqamni o'zgartirish")],
        [KeyboardButton(text='🔝 Asosiy Menyu')]

    ],
    resize_keyboard=True
)

@dp.message_handler(text="⚙️ Sozlamalar")
async def bot_start(message: types.Message):
    await message.answer(f"<b>⚙️ Sozlamalar</b>" , reply_markup=sozlama)

@dp.message_handler(text="Ismni o'zgartirish")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Tez kunda...</b>" , reply_markup=sozlama)

@dp.message_handler(text="Raqamni o'zgartirish")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Tez kunda...</b>" , reply_markup=sozlama)


nomer_update = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="☎️ Telfon jo'nating", request_contact=True)]

    ],
    resize_keyboard=True
)


royxat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Ro'yxatdan o'tish ➕", request_contact=True)]

    ],
    resize_keyboard=True
)

tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Tasdiqlash"),
            KeyboardButton(text="❌ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

tasdiqtaklif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Xa"),
            KeyboardButton(text="❌ Yo'q")
        ]
    ],
    resize_keyboard=True
)