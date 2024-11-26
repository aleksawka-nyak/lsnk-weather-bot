from aiogram import Router
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.api.exceptions import NoContextError
from loguru import logger

from telegram_bot.dialogs.states import Forecast, Main

router = Router()


@router.message()
async def city_handler(message: Message, dialog_manager: DialogManager):
    try:
        dialog_manager.dialog_data.clear()
    except NoContextError:
        logger.warning("Dialog manager was not presented")
    city = message.text.strip()
    logger.info(f"City received: {city}")
    await dialog_manager.start(Forecast.MAIN, data={"city": city} , mode = StartMode.RESET_STACK)
