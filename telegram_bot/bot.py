import asyncio
from aiogram_dialog import setup_dialogs

from dialogs import dialogs
from handlers import routers
from loguru import logger
from config import TELEGRAM_BOT_TOKEN
from aiogram import Bot, Dispatcher

logger.add("logs/bot.log", rotation="10 MB")
dispatcher = Dispatcher()

async def on_startup(dispatcher: Dispatcher):
    logger.success("Бот запущен")


async def on_shutdown(dispatcher: Dispatcher):
    logger.success("Бот остановлен")

def include_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(*routers)
    dispatcher.include_routers(*dialogs)

async def main():
    bot_token = TELEGRAM_BOT_TOKEN
    bot: Bot = Bot(token=bot_token)

    #dispatcher = Dispatcher()
    include_routers(dispatcher)
    setup_dialogs(dispatcher)
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)


    try:
        await dispatcher.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Работа программы принудительно завершена")
