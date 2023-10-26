import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config #Secret Token
from aiogram import html
from handlers import questions, games, group_games, usernames, different_types #My handlers

async def main():
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="html")
    dp = Dispatcher()

    dp.include_routers(questions.router, games.router, group_games.router, usernames.router, different_types.router)
    # dp.include_router(questions.router)
    # dp.include_router(group_games.router)
    # dp.include_router(different_types.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("Let's start!\n")
    asyncio.run(main())
