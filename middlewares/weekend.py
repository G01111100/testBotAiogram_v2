from datetime import datetime
from typing import Callable, Dict, Any, Awaitable
from aiogram.dispatcher.flags import get_flag #For flags
from aiogram.utils.chat_action import ChatActionSender #For flahs

from aiogram import  BaseMiddleware
from aiogram.types import Message, CallbackQuery

def _isweekend() -> bool:
    # 5 - Saturday, 6 - Sunday
    return datetime.utcnow().weekday() in (5, 6, 0)

# Это будет inner-мидлварь на сообщения
class WeekendMessageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        # Если сегодня не суббота и не воскресенье,
        # то продолжаем обработку.
        if not _isweekend():
            return await handler(event, data)
        # В противном случае просто вернётся None
        # и обработка прекратится
        await event.answer("This command doesn't work on weekends!")
        return

# Это будет outer-мидлварь на любые колбэки
class WeekendCallbackMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        # Если сегодня не суббота и не воскресенье,
        # то продолжаем обработку.
        if not _isweekend():
            return await handler(event, data)
        # В противном случае отвечаем на колбэк самостоятельно
        # и прекращаем дальнейшую обработку
        await event.answer("Bot doesn't work on weekends!", show_alert=True)
        return

#Work with flags
class ChatActionMiddleware(BaseMiddleware):
    def __init__(self, bot):
        self.bot = bot

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        long_operation_type = get_flag(data, "long_operation")

        #Если такого флага на хэндлера нет
        if not long_operation_type:
            # print("BEFORE long_operation = FALSE")
            return await handler(event, data)

        #Если флаг есть
        # print("BEFORE long_operation = TRUE")
        async with ChatActionSender(
            bot=self.bot,
            action=long_operation_type,
            chat_id=event.chat.id
        ):
            return await handler(event, data)
