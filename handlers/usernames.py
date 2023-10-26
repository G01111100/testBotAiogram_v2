from typing import List

from aiogram import Router, F
from aiogram.types import Message

from filters.find_username import HasUsernamesFilter

router = Router()

@router.message(F.text, HasUsernamesFilter())
async def message_with_usernames(message: Message, usernames: List[str]):
    await message.reply(f'Thanks! Of course I\'ll subscribe to {", ".join(usernames)}!')