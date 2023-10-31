from aiogram import Router, F
from aiogram import html
from aiogram.types import Message, Chat, PhotoSize
from datetime import datetime #Time link

router = Router()

@router.message(F.forward_from_chat[F.type == "channel"].as_("channel"))
async def forwarded_from_channel(message: Message, channel: Chat):
    await message.answer(f"This channel's ID is {channel.id}")

@router.message(F.text)
async def message_with_text(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a text message!\nYour message:</b>\n\t\t\t{message.html_text}\n\n{time_link_text}")

@router.message(F.document)
async def message_with_file(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a document!</b>\n\n{time_link_text}")

@router.message(F.photo[-1].as_("last_photo"))
async def forward_from_channel_handler(message: Message, last_photo:PhotoSize) -> None:
    # print(largest_photo.width, largest_photo.height)
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a photo (<code>{last_photo.width} * {last_photo.height}</code>)!</b>\n\n{time_link_text}")

# @router.message(F.photo)
# async def message_with_photo(message: Message):
#     time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
#     await message.answer(f"<b>This is a photo!</b>\n\n{time_link_text}")

@router.message(F.sticker)
async def message_with_sticker(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a sticker!</b>\n\n{time_link_text}")

@router.message(F.animation)
async def message_with_animation(message: Message):
    time_link_text = html.underline(f"Created at {datetime.now().strftime('%H:%M')}!")
    await message.answer(f"<b>This is a GIF!</b>\n\n{time_link_text}")
