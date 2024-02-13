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

     await bot.send_message(chat_id='-1001829161444', text=f"{taklif}")
     await state.finish()