from aiogram import types
from loader import dp, db, bot
from aiogram.types.web_app_info import WebAppInfo

db.create_table_users()

@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    if message.chat.type == 'private':
        user_id = message.from_user.id
        full_name = message.from_user.full_name
        if not db.user_exists(user_id):
            db.add_fullname(user_id=user_id, full_name=full_name)

    await message.answer(f"AssalomuAlaykum {message.from_user.full_name}")


@dp.message_handler(commands='open_page')
async def open_page_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Open Web Page", web_app=WebAppInfo(url='https://cybernation.uz/')))
    await message.answer("Click the button below to open our website:", reply_markup=keyboard)


async def on_startup(dp):
    await bot.set_webhook("https://cybernation.uz/")

async def on_shutdown(dp):
    await bot.delete_webhook()


    # text = ("@haad_uz Programming and Cyber & Security Learning Center!\n",
    #         "<b>Asosiy:</b>",
    #         "/start - Botni Ishga Tushirish\n"
    #         "/help - Shu Habarni Ko'rsatadi\n\n"
    #         "<b>Biz Haqimizda:</b>\n"
    #         "/aboutus - Biz Haqimizda\n"
    #         "/aboutadresses - Bizning manzillar\n\n"
    #         "<b>Bizning Kurslar Haqida Ma'lumot:</b>\n"
    #         "/cybernation - Cybernation Kursi\n"
    #         "/cybersecurity - CyberSecurity Kursi\n"
    #         "/netbackend - .NET BackEnd Kursi\n"
    #         "/robohack - Robohack Kursi\n"
    #         "/flutter - Flutter Kursi\n\n"
    #         "<b>Kurslarga Ro'yxatdan O'tish:</b>\n"
    #         "/register - Kurslarga Yozilish\n",
    #         "<b>Sifat nazorati:</b>\n"
    #         "/suggest - Taklif Va Shikoyat Uchun")

    # await message.answer("\n".join(text))
