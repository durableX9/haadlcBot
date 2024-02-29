from aiogram import Bot, Dispatcher, types


from data import config
from utils.db_api.db import Database

bot = Bot(token=config.BOT_TOKEN)
# storage = MemoryStorage()
dp = Dispatcher(bot)
db = Database()