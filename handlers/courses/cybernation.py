from aiogram import types

from loader import dp

@dp.message_handler(commands='cybernation')
async def cybernation_com(message: types.Message):
    await message.answer("Cybernation kursi haqida to'liq ma'lumot uchun quyidagi tugmadan foydalaning!")