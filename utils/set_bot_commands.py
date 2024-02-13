from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni Ishga Tushirish"),
            types.BotCommand("help", "Botni Ishlatish Uchun Ko'rsatma"),
            types.BotCommand("aboutus", "Biz Haqimizda"),
            types.BotCommand("aboutadresses", "Bizning Manzillar"),
            types.BotCommand("cybernation", "Cybernation Kursi Haqida Ma'lumot"),
            types.BotCommand("cybersecurity", "CyberSecurity Kursi Haqida Ma'lumot"),
            types.BotCommand("netbackend", " NET BackEnd Kursi Haqida Ma'lumot"),
            types.BotCommand("robohack", "Robohack Kursi Haqida Ma'lumot"),
            types.BotCommand("flutter", "Flutter Kursi Haqida Ma'lumot"),
            types.BotCommand("suggest", "Taklif Va Shikoyat Uchun")
        ]
    )
