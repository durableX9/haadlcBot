from aiogram.types import Message

from aiogram import types
from loader import dp

@dp.message_handler(commands='help')
async def bot_help(message: types.Message):
    text = ("@haad_uz Programming and Cyber & Security Learning Center!\n",
            "<b>Asosiy:</b>",
            "/start - Botni Ishga Tushirish\n"
            "/help - Shu Habarni Ko'rsatadi\n\n"
            "<b>Biz Haqimizda:</b>\n"
            "/aboutus - Biz Haqimizda\n"
            "/aboutadresses - Bizning manzillar\n\n"
            "<b>Bizning Kurslar Haqida Ma'lumot:</b>\n"
            "/cybernation - Cybernation Kursi\n"
            "/cybersecurity - CyberSecurity Kursi\n"
            "/netbackend - .NET BackEnd Kursi\n"
            "/robohack - Robohack Kursi\n"
            "/flutter - Flutter Kursi\n\n"
            "<b>Kurslarga Ro'yxatdan O'tish:</b>\n"
            "/register - Kurslarga Yozilish\n",
            "<b>Sifat nazorati:</b>\n"
            "/suggest - Taklif Va Shikoyat Uchun")

    await message.answer("\n".join(text))
