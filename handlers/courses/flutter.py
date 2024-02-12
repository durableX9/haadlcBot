from aiogram import types   
from aiogram.types import Message

from loader import dp, bot
from keyboards.inline.cybernation_kb import cybernation_kb


@dp.message_handler(commands='flutter')
async def cybernation_com(message: types.Message):
    await message.reply("Flutter kursi haqida to'liq ma'lumot olish uchun quyidagi tugmadan foydalaning!", reply_markup=cybernation_kb)

    next_suggest = ("Agarda siz flutter kursi haqida ma'lumotni <b>video shaklida</b> ko'rmoqchi bo'lsangiz /flutter_video buyrug'ini bering")
    await message.answer(next_suggest)


@dp.message_handler(commands='flutter_video')
async def cyber_video(message: Message):
    video1 = 'BAACAgUAAxkBAANdZcnjES-zXP-E_WKf2xWBKSm37SsAAtcNAAJCyFBWOy03foKbWEk0BA'
    await bot.send_video(chat_id=message.chat.id, video=video1)
