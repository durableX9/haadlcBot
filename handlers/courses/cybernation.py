from aiogram import types

from loader import dp, bot
from keyboards.inline.cybernation_kb import cybernation_kb
from aiogram.types import callback_query, CallbackQuery

@dp.message_handler(commands='cybernation')
async def cybernation_com(message: types.Message):
    await message.reply("Cybernation kursi haqida to'liq ma'lumot uchun quyidagi tugmadan foydalaning!", reply_markup=cybernation_kb)
