from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp,db


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    id = message.chat.id
    lang =db.select_lang(id=id)
    if lang[1] == 'eng':
        await message.answer("<b>Commands:</b> \n/start - Restart\n/lang - Choose a Language \n/help - Help")
    if lang[1] == 'rus':
        await message.answer("<b>Команды:</b> \n/start - Запустить бота\n/lang - Выберите язык\n/help - Помощь")
    if lang[1] == 'uzb':
        await message.answer("<b>Buyruqlar:</b> \n/start - Botni ishga tushirish\n/lang - Til tanlash\n/help - Yordam")
    if lang[1] == 'turk':
        await message.answer("<b>Komutlar:</b> \n/start - Botu başlat\n/lang - Bir Dil Seçin\n/help - Yardım Edin")