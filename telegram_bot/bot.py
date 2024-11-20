import asyncio

from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent
from aiogram.types import ReplyKeyboardRemove
from aiogram_dialog import setup_dialogs, DialogManager
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram_dialog.api.exceptions import UnknownIntent
from aiogram_dialog import StartMode
from aiogram_dialog import ShowMode

from dialogs import dialogs
from handlers import routers
from loguru import logger
from config import TELEGRAM_BOT_TOKEN
from aiogram import Bot, Dispatcher
from telegram_bot.dialogs import states


logger.add("logs/bot.log", rotation="10 MB")


async def on_startup(dispatcher: Dispatcher):
    logger.success("Бот запущен")


async def on_shutdown(dispatcher: Dispatcher):
    logger.success("Бот остановлен")


def include_routers(dispatcher: Dispatcher):
    dispatcher.include_routers(*routers)
    dispatcher.include_routers(*dialogs)


async def main():
    bot_token = TELEGRAM_BOT_TOKEN
    bot: Bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode="MarkDown"))

    dispatcher = Dispatcher()
    include_routers(dispatcher)
    setup_dialogs(dispatcher)
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_shutdown)
    dispatcher.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent),
    )

    try:
        await dispatcher.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


async def on_unknown_intent(event: ErrorEvent, dialog_manager: DialogManager):
    logger.error(f"Restarting dialog: {event.exception}")
    if event.update.callback_query:
        await event.update.callback_query.answer(
            "Бот перезапущен, ввиду технической неполатки.\n"
            "Возврат в главное меню...",
        )
        if event.update.callback_query.message:
            try:
                await event.update.callback_query.message.delete()
            except TelegramBadRequest:
                pass  # whatever
    elif event.update.message:
        await event.update.message.answer(
            "Бот перезапущен, ввиду технической неполатки.\n"
            "Возврат в главное меню...",
            reply_markup=ReplyKeyboardRemove(),
        )
    await dialog_manager.start(
        states.Main.MAIN,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND,
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Работа программы принудительно завершена")
