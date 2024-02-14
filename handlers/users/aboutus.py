import asyncio
from loader import dp
from aiogram.types import Message

@dp.message_handler(commands=['aboutus'])
async def about_us(message: Message):
    text1 = ("Haad Learning Center - <b>Kiberxavfsizlik</b> va <b>Dasturlashga</b> ixtisoslashgan markaz.\n\n"
            "⚡️ Hozirgi vaqtda  Haad LC markazida <b>500+/-</b> ortiq talabalar <b>dasturlash</b> va <b>kiberhavfsizlik</b> yo'nalishlari bo'yicha ta'lim olib kelishadi.\n\n"
            "Markazimizning asosiy maqsadlaridan biri <b>O'zbekistonda kiberhavfsizlik sohasini rivojlantirish</b> va talabarimizdan dunyo standartlariga javob bera oladigan <b>mutaxasislar yetishishtirib chiqish</b>.")
   
    await message.answer(text1)


    text2 = ("@haad_uz Programming and Cyber & Security Learning Center!\n",
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
    
    await asyncio.sleep(15)
    await message.answer("\n".join(text2), parse_mode='HTML')