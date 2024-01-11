from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.inline.location_button import location_keys
from loader import dp

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(Command("resturant"))
async def gets(message: types.Message):
    await message.answer(text="Restoran",reply_markup=location_keys)
