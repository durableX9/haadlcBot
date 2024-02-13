from aiogram.dispatcher.filters.state import StatesGroup, State

class RegisterMan(StatesGroup):
    name_sur = State()
    number = State()
    target = State()
