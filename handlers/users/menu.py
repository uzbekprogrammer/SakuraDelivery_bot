from aiogram import types
from aiogram.types import ForceReply

from loader import dp


@dp.message_handler(text='✍️ Izoh va takliflar')
async def izoh(message: types.Message):
    await message.answer('Izoh va takliflaringiz bo\'lsa yozib qoldirishingiz mumkin',
                         reply_markup=ForceReply())
