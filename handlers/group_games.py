from aiogram import Router
from aiogram import F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command
from filters.chat_type import ChatTypeFilter

router = Router()
# router.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"])) #with ChatTypeFilter
router.message.filter(F.chat.type.in_({"group", "supergroup"}))


@router.message(Command("gdice"))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

@router.message(Command("gdart"))
async def cmd_dart_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DART)

@router.message(Command("gbasketball"))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)

@router.message(Command("gfootball"))
async def cmd_football_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)

@router.message(Command("gslot_machine"))
async def cmd_slot_machine_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.SLOT_MACHINE)

@router.message(Command("gbowling"))
async def cmd_bowling_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)

# @router.message(ChatTypeFilter(chat_type=["group", "supergroup"]), Command(commands="dice"))
# async def cmd_dice_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.DICE)
#
# @router.message(ChatTypeFilter(chat_type=["group", "supergroup"]), Command(commands="basketball"))
# async def cmd_basketball_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.BASKETBALL)
