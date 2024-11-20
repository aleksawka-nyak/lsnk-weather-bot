from aiogram import Router
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from loguru import logger

from telegram_bot.dialogs.states import Forecast

router = Router()


@router.message()
async def city_handler(message: Message, dialog_manager: DialogManager):
    dialog_manager.dialog_data.clear()
    city = message.text.strip()
    logger.info(f"City received: {city}")
    dialog_manager.dialog_data["city"] = city
    await dialog_manager.start(Forecast.MAIN, data={"city": city} , mode = StartMode.RESET_STACK)
