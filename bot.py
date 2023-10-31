import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config #Secret Token
from aiogram import html

from handlers import bot_in_group, in_pm, questions, checkin, games, group_games, usernames, different_types #My handlers
from middlewares.weekend import WeekendCallbackMiddleware, WeekendMessageMiddleware, ChatActionMiddleware

botM = Bot(token=config.bot_token.get_secret_value(), parse_mode="html")

async def main():

    dp = Dispatcher()

    dp.callback_query.outer_middleware(WeekendCallbackMiddleware())
    dp.message.middleware(ChatActionMiddleware(botM))
    # dp.message.middleware(WeekendMessageMiddleware())

    # dp.include_routers(questions.router, games.router, group_games.router, usernames.router, different_types.router)
    dp.include_router(bot_in_group.router)
    dp.include_router(in_pm.router)
    dp.include_router(questions.router)
    dp.include_router(checkin.router)
    dp.include_router(games.router)
    dp.include_router(group_games.router)
    dp.include_router(usernames.router)
    dp.include_router(different_types.router)

    await botM.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(botM)

if __name__ == '__main__':
    print("Let's start!\n")
    asyncio.run(main())
