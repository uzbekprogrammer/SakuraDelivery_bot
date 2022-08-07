from aiogram.types import Message
import requests
from loader import dp
from states import get_num


@dp.message_handler(state=get_num.Number)
async def parol(message: Message):
    phonenum = int(message.text)
