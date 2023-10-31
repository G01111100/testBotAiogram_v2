import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.checkin import get_checkin_kb
from middlewares.weekend import WeekendMessageMiddleware, ChatActionMiddleware

router = Router()
router.message.filter(F.chat.type == "private")
# router.message.middleware(WeekendMessageMiddleware())
# router.message.outer_middleware(ChatActionMiddleware())
# router.callback_query.middleware(WeekendMessageMiddleware())

# typing for text messages,
# upload_photo for photos,
# record_video or upload_video for videos,
# record_voice or upload_voice for voice notes,
# upload_document for general files,
# choose_sticker for stickers,
# find_location for location data,
# record_video_note or upload_video_note for video notes.
@router.message(Command("checkdelay"), flags={"long_operation": "typing"})#"upload_video_note"})
async def cmd_checkdelay(message: Message):
    await message.answer("Start of delay!")
    N = 60
    step = 15
    for i in range(0, N, step):
        await message.answer(f"{N-i} sec...")
        await asyncio.sleep(step)
    await message.answer("End of delay!")

@router.message(Command("checkin"))
async def cmd_checkin(message: Message):
    await message.answer("Please, click on the button below", reply_markup=get_checkin_kb())

@router.callback_query(F.data == "confirm")
async def checkin_confirm(callback: CallbackQuery):
    await callback.answer("Thanks, confirm!", show_alert=True)
    await callback.answer()
