from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

location_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Найти отели поблизости ", callback_data="mylocation"),
        ],
    ],
)