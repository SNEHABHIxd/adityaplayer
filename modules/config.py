import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", "1659876787"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "AdityaHalder")
BOT_USERNAME = getenv("BOT_USERNAME", "AdityaProbot")
BOT_TOKEN = getenv("BOT_TOKEN", "token")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/b68d40fc2759ea46277b3.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("SESSION_NAME", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1659876787").split()))
