from aiogram import Router, F
from aiogram import html
from aiogram.types import Message
from datetime import datetime #Time link

router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a text message!\nYour message:</b>\n\t\t\t<i>{message.text}</i>\n\n{time_link_text}")

@router.message(F.photo)
async def download_photo(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a photo!</b>\n\n{time_link_text}")

@router.message(F.sticker)
async def message_with_text(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a sticker!</b>\n\n{time_link_text}")

@router.message(F.animation)
async def message_with_text(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a GIF!</b>\n\n{time_link_text}")
