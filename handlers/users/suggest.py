from states.suggestion import hisSuggestForUs
from loader import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='suggest', state=None)
async def start_suggest(message: types.Message, state: FSMContext):
     await bot.send_message(chat_id=message.chat.id, text="Iltimos taklif yoki shikoyatingizni yozib qoldiring.")
     await hisSuggestForUs.write.set()

@dp.message_handler(state=hisSuggestForUs.write)
async def procces_write(message: types.Message, state: FSMContext):
     write = message.text
     await state.update_data(write=write)

     await bot.send_message(chat_id=message.chat.id, text="Sizning qoldirgan taklif va shikoyatingiz o'rganib chiqiladi va unga yechim topishga harakat qilamiz 😊")

     taklif = f"<b>Foydalanuvchidan kelgan taklif yoki shikoyat:</b> {write}"

     await bot.send_message(chat_id='-1002103258715', text=f"{taklif}")
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

     await state.finish()
