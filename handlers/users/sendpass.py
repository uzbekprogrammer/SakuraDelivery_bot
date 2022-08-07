import requests
import time


async def sendpass(number):
    n = requests.post('https://www.tashkent.uz/uz/virtual-send-code?phone=XXxxxxxxx&isSend=true')
    return n
