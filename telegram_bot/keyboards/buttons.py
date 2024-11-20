from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

cities = ["Москва",
          "Краснодар",
          "Санкт-Петербург"
]


async def favourite_builder(message: types.Message, city: str):
    """
    Добавляет текущий город в избранное
    :param message: Сообщение, к которому прикреплена клавиатура
    :param city: Текущий город
    :return: Клавиатура "избранных" городов
    """
    builder = ReplyKeyboardBuilder()
    cities.insert(0, city)

    for city in cities[:3]:
        builder.add(types.KeyboardButton(text=city))
    await message.answer(
        f"Город {cities[0]} добавлен в избранное",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )
