import bot
from aiogram import F, Router
from aiogram.filters.chat_member_updated import \
    ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER, ADMINISTRATOR, KICKED
from aiogram.types import ChatMemberUpdated

router = Router()
router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> MEMBER))
async def bot_added_as_member(event: ChatMemberUpdated):
    # Бота добавили как участника
    chat_info = await bot.botM.get_chat(event.chat.id)
    if chat_info.permissions.can_send_messages:
        await  event.answer(
            text=f"Hello! Thanks for adding me to "
                 f"{event.chat.type} '{event.chat.title}' "
                 f"as a member. CHAT_ID: {event.chat.id}"
        )
    else:
        print("Another time!")

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> ADMINISTRATOR))
async def bot_added_as_admin(event: ChatMemberUpdated):
    await event.answer(
        text=f"Hello! Thanks for adding me to "
             f"{event.chat.type} '{event.chat.title}' "
             f"as an administrator. CHAT_ID: {event.chat.id}"
    )

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER >> ADMINISTRATOR))
async def bot_added_as_admin(event: ChatMemberUpdated):
    await event.answer(
        text=f"Thank you for promotion to administrator in the "
             f"{event.chat.type} '{event.chat.title}' "
             f"CHAT_ID: {event.chat.id}"
    )

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR >> MEMBER))
async def bot_added_as_admin(event: ChatMemberUpdated):
    await event.answer(
        text=f"It is sad to be an ordinary member in the "
             f"{event.chat.type} '{event.chat.title}' "
             f"CHAT_ID: {event.chat.id}"
    )

#Don't work
@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER >> KICKED))
async def bot_added_as_admin(event: ChatMemberUpdated):
    await event.answer(
        text=f"It is sad to left from "
             f"{event.chat.type} '{event.chat.title}' as member "
             f"CHAT_ID: {event.chat.id}"
    )

@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=ADMINISTRATOR >> KICKED))
async def bot_added_as_admin(event: ChatMemberUpdated):
    await event.answer(
        text=f"It is so sad to left from "
             f"{event.chat.type} '{event.chat.title}' as administrator"
             f"CHAT_ID: {event.chat.id}"
    )