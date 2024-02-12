from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram import types
from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp


@dp.message_handler(commands=['aboutadresses'])
async def show_contact_keys(message: Message):
    await message.answer(text="Lokatsiya yuboring:", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_contact(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n<b>Masofa:</b> {distance:.1f} km."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"Lokatsiya yuborganingiz uchun rahmat <b>sizning masofangizdan</b> <b>HAAD LC</b> masofasigacha bo'lgan oraliq. \n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
        