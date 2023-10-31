from aiogram import Router
from aiogram import F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command
from filters.chat_type import ChatTypeFilter

from middlewares.weekend import WeekendMessageMiddleware

router = Router()
# router.message.filter(ChatTypeFilter(chat_type=["private"])) #with ChatTypeFilter
router.message.filter(F.chat.type.in_({"private"}))
# router.message.middleware(WeekendMessageMiddleware())

@router.message(Command("dice"))
async def cmd_dice(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

@router.message(Command("dart"))
async def cmd_dart(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DART)

@router.message(Command("basketball"))
async def cmd_basketball(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)

@router.message(Command("football"))
async def cmd_football(message: Message):
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)

@router.message(Command("slot_machine"))
async def cmd_slot_machine(message: Message):
    await message.answer_dice(emoji=DiceEmoji.SLOT_MACHINE)

@router.message(Command("bowling"))
async def cmd_bowling(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)

