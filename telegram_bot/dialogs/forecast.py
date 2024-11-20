from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format
from loguru import logger
from magic_filter import F

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
    logger.info(f"city in getter is {city}")
    if not city:
        logger.warning("City not found in dialog_data. Please check city_handler.")
        return {"forecast": "Не удалось получить данные о погоде."}
    logger.info(f"Fetching weather for city in get_forecast: {city}")
    weather = 'lsnk-weather-bot ' + (await  forecast_parser(city))

    markdown_weather = f"```{weather}```"

    return {
        "forecast": markdown_weather
    }

dialog = Dialog(
    Window(
        Format("{forecast}"),
        Button(
            Const("В избранное"),
            id="favourite",
            on_click=add_favourite,
            when=F["city"]
        ),
        state=states.Forecast.MAIN,
        getter=get_forecast
    )
)