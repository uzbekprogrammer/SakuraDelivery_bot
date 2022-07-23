from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Buyurtma berish"),
        ],
        [
            KeyboardButton(text='ℹ️ Ma\'lumot'),
            KeyboardButton(text='✍️ Izoh va takliflar')
        ],
    ],
    resize_keyboard=True,
)
