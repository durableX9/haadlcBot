from aiogram import types
from loader import dp

@dp.message_handler(commands='start')
async def start_button(message: types.Message):
    await message.answer(f"AssalomuAlaykum {message.from_user.full_name}")