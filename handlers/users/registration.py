from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from loader import dp, bot
from states.register import RegisterMan
from keyboards.default.contact import markup_request
from data.config import CHANNEL_REG

@dp.message_handler(commands='register')
async def register(message: Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text="<b>Haad LC`dan</b> ro'yxatdan o'tish uchun iltimos ismingizni yuboring:") 
    
    await RegisterMan.name_sur.set()


@dp.message_handler(state=RegisterMan.name_sur)
async def his_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    name = message.text
    await state.update_data(name=name)
    await bot.send_message(chat_id=message.chat.id, text="Iltimos endi telefon raqamingizni yuboring", reply_markup=markup_request)

    await RegisterMan.number.set()


@dp.message_handler(state=RegisterMan.number)
async def his_number(message: Message, state: FSMContext):
    if message.contact:
        async with state.proxy() as data:
            data['contact'] = message.contact.phone_number

        # Get the collected data
        state_data = await state.get_data()

        # Send the collected data to your channel
        await bot.send_message(chat_id=CHANNEL_REG[0],
                               text=f"Keldi:\nIsm-Sharif: {state_data['name']}\nTelefon-raqam: {state_data['contact']}")
        
        await bot.send_message(chat_id=message.from_user.id, text="Yuborganingiz uchun rahmat", reply_markup=ReplyKeyboardRemove())
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Kechirasiz, siz kontakt jo'natmadingiz. Iltimos, telefon raqamingizni jo'nating.")
    
    await state.finish()
