from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)


keybord_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="java")],
    [KeyboardButton(text="python")],
    [KeyboardButton(text="javascript")],
])


inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")],
    [InlineKeyboardButton(text="Начать игру", callback_data="quiz_start")]
])