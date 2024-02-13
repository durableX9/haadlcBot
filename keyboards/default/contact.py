from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from loader import dp, bot

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Kontaktingizni yuboring 📲", request_contact=True)
)