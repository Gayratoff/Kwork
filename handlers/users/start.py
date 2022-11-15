from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from utils.db_api.sqlite import *
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.menu import menuuz,menuru, menuen,royxat,buyurtma,frilans
from  keyboards.inline.lang import laguage, laguageen, laguageru,laguageuz

langa = f"<b>🌍 Choose a Language :</b>"

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        id =message.from_user.id
        nomer = db.select_royxat(id=id)
        if nomer[1] == message.contact:
            pass

        else:
            await message.answer("<b>NEED WORK botiga xush kelibsiz</b>", reply_markup=menuuz)

    except:
        await message.answer("Bot ishlashi uchun <b>➕ Ro'yxatdan o'tish ➕</b> tugmasini bosin", reply_markup=royxat)

@dp.message_handler(content_types=['contact'])
async def phone_number(message: types.Message):
    nick_name = message.contact.full_name
    id = message.contact.user_id
    phone_usm = message.contact.phone_number
    try:
        db.royxat_qoshish(id=id,
            number=phone_usm, nick_name=nick_name)
    except:
        pass
    await message.answer("<b>Yaxshi endi botdan foidalanishingiz mumkin</b>", reply_markup=menuuz)


@dp.message_handler(text="📝 Mening  buyurtmalarim")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_zakaz(tg_id=user_id)
        for idsend in id_send:
            sql_id = idsend[1]
            await message.answer(f"{sql_id}",reply_markup=frilans)
    except:
        pass
    await message.answer(f"<b>Sizning buyurtmalaringiz</b>" , reply_markup=frilans)

@dp.message_handler(text="📝 Mening buyurtmalarim")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_zakaz(tg_id=user_id)
        for idsend in id_send:
            sql_id = idsend[1]
            await message.answer(f"{sql_id}",reply_markup=buyurtma)
    except:
        pass
    await message.answer(f"<b>Sizning buyurtmalaringiz</b>" , reply_markup=buyurtma)


@dp.message_handler(text="📥 Buyurtma olish")
async def bot_start(message: types.Message):
    users = db.select_random_zakaz()
    print(users,"buyurtmalar")
    for user in users:
        user_id= user[1]
        ms_id = user[0]
        inline_tugma = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Taklif kiritish", callback_data=f'taklif{ms_id}')]])
        await  message.answer(text=f"{user_id}",reply_markup=inline_tugma)


@dp.message_handler(text="✅ Freelancer takliflar")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_taklifs(tg_id=user_id)
        for idsend in id_send:
            sql_id = idsend[2]
            await message.answer(f"{sql_id}",reply_markup=buyurtma)
    except:
        pass
    await message.answer(f"<b>✅ Freelancer takliflar 👆👆👆</b>" , reply_markup=buyurtma)

@dp.message_handler(text="✅ Mening takliflarim")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_taklifs(Tid=user_id)
        for idsend in id_send:
            sql_id = idsend[2]
            await message.answer(f"{sql_id}",reply_markup=frilans)
    except:
        pass
    await message.answer(f"<b>✅ Sizning takliflaringiz 👆👆👆</b>" , reply_markup=frilans)
