import requests
from pyrogram import idle
from pyrogram import Client as Bot

from modules.Client.callsmusic import run
from modules.config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

response = requests.get(BG_IMAGE)
with open("./resource/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

bot.start()
run()
idle() 
