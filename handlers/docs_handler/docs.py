from loader import dp
from aiogram.types import ContentType, Message


@dp.message_handler()
async def text_handler(message: Message):
    await message.reply('Siz Matn Yubordingiz!')

@dp.message_handler(content_types=ContentType.VIDEO)
async def doc_handler(message: Message):
    await message.video.download()
    await message.reply("<b>Video Qabul Qilindi Ammo Siz Video yubordingiz!\n</b>"
                        f"file_id = {message.video.file_id}")
    