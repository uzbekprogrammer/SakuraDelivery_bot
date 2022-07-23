import asyncio
import re

from aiogram import types

from aiogram.dispatcher.filters import Command
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    for user in users:
        # print(user[3])
        user_id = user[3]
        print(user)
        await bot.send_message(
            chat_id=user_id, text="@BadBoy_dev kanaliga obuna bo'ling!"
        )
        await asyncio.sleep(0.05)


@dp.message_handler(commands='allusers', user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = await db.select_all_users()
    response = ''
    # await message.reply(len(users))
    print(users)
    for user in users:
        response += f'{user[1]}\n'
    await message.reply(response)


@dp.message_handler(commands="cleandatabase", user_id=ADMINS)
async def get_all_users(message: types.Message):
    await db.delete_users()
    await message.answer("Baza tozalandi")


@dp.message_handler(commands="rek", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    ketgan = []
    for user in users:
        user_id = user[0]
        # print(f"user_id{user}\nuser={user}\nADMINS={ADMINS}")
        try:
            await message.reply_to_message.copy_to(chat_id=user_id, reply_markup=message)
            ketgan.append(user_id)
        except:
            pass
        # await bot.send_message(chat_id=1361934966, text=msg)
        await asyncio.sleep(0.5)
    await bot.send_message(chat_id=1768033194, text=f"{ketgan}\n\n{len(ketgan)} ta userga yuborildi")


@dp.message_handler(commands="menu", user_id=ADMINS)
async def show_handlers(message: types.Message):
    await message.answer("/allusers - Hamma foydalanuvchilarni chiqaradi\n"
                         "/rek - Reklama uchun\n"
                         "cleandatabase - Ehtiyot boling"
                         "!send - ID raqam yozilgan odamga jonatildi"
                         "!who - ID raqamli odamni topib beradi")


@dp.message_handler(Command("who", prefixes='!#'), user_id=ADMINS)
async def search_user(message: types.Message):
    command_parse = re.compile(r"(!who|#who) ?(\d+)?")
    parsed = command_parse.match(message.text)
    user_id = int(parsed.group(2))
    users = await db.select_all_users()
    for user in users:
        if user_id in user:
            await message.reply(f'<a href="tg://user?id={user_id}">{user[1]}</a> topildi.')
            break
    loop = await message.reply("Usernot found")
    await asyncio.sleep(5)
    await loop.delete()


@dp.message_handler(Command("send", prefixes='!#'), user_id=ADMINS)
async def search_user(message: types.Message):
    command_parse = re.compile(r"(!send|#send) ?(\d+)?")
    parsed = command_parse.match(message.text)
    user_id = int(parsed.group(2))
    try:
        await message.reply_to_message.copy_to(chat_id=user_id, reply_markup=message)
        await message.answer("Muvaffaqiyatli jonatildi")
    except:
        await message.answer("Jonatib bolmadi!\nUser botni blocklagan")