from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format
from aiohttp import ClientResponseError
from loguru import logger

from telegram_bot.keyboards.buttons import favourite_builder
from telegram_bot.dialogs import states
from telegram_bot.parser import forecast_parser


async def add_favourite(callback: CallbackQuery, button: Button, manager: DialogManager):
    """
    Добавляет текущий город в избранное
    """
    city = manager.start_data["city"]
    logger.info(f"{city} is added to favourites")
    await favourite_builder(callback.message, city)


async def get_forecast(dialog_manager: DialogManager, **kwargs):
    """
    Получает прогноз погоды для заданного города
    """
    city = dialog_manager.start_data["city"]
    try:
        message = await forecast_parser(city)
        success = True
    except ClientResponseError as e:
        if e.status == 404:
            message = "Город не найден."
            success = False
        else:
            message = "Не удалось получить данные о погоде."
            success = False
    markdown_message = f"```lsnk-weather-bot\n{message}```"
    response = {"success": success, "forecast": markdown_message}
    logger.debug(f"Forecast for {city} received: {response}")
    return response


dialog = Dialog(
    Window(
        Format("{forecast}"),
        Button(
            Const("В избранное"),
            id="favourite",
            on_click=add_favourite,
            when="success",
        ),
        state=states.Forecast.MAIN,
        getter=get_forecast
    )
)