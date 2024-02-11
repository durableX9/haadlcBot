from aiogram import types
from loader import dp, db, bot

db.create_table_users()

@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    if message.chat.type == 'private':
        user_id = message.from_user.id
        full_name = message.from_user.full_name
        if not db.user_exists(user_id):
            db.add_fullname(user_id=user_id, full_name=full_name)

    await message.answer(f"AssalomuAlaykum {message.from_user.full_name}")
