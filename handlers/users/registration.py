from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from loader import dp, bot
from states.register import RegisterMan
from keyboards.default.contact import markup_request

@dp.message_handler(commands='register', state=None)
async def start_register(message: Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id, text="Iltimos ismingiz va familayangizni yozib qoldiring.")
    await RegisterMan.name_sur.set()

@dp.message_handler(state=RegisterMan.name_sur)
async def procces_write(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await bot.send_message(chat_id=message.chat.id, text="Iltimos endi kontaktingizni yuboring", reply_markup=markup_request)
    await RegisterMan.number.set()

@dp.message_handler(content_types=ContentTypes.CONTACT ,state=RegisterMan.number)
async def procces_number(message: Message, state: FSMContext):
    number = message.contact.phone_number
    await state.update_data(number=number)
    await bot.send_message(chat_id=message.from_user.id, text="Raqamingiz qabul qilindi 😊", reply_markup=ReplyKeyboardRemove())

    data = await state.get_data()
    result = (f"<b>Foydalanuvchidan kelgan result:</b>\n\n"
              f"{data.get('name', 'N/A')}\n\n"
              f"{data.get('number', 'N/A')}\n\n")

    await bot.send_message(chat_id='-1002038231507', text=result, parse_mode="HTML")
    await state.finish()
