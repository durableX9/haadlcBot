# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# cybernation_kb = InlineKeyboardButton("Batafsil ma'lumot", url='https://telegra.ph/CyberNation-0tio4', callback_data='cybernation_kb')
# start_keyboard = InlineKeyboardMarkup(resize_keyboard=True).add(cybernation_kb)
# cybernation_kb.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cybernation_kb = InlineKeyboardMarkup(resize_keyboard=True)
cybernation_kb.add(InlineKeyboardButton("Batafsil ma'lumot", url='https://telegra.ph/CyberNation-08-04'))
