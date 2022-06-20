## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBQTaoEhSHMcZzLGgIxZ67__IvEtIyT9Ct5vOKaoiWIbkSKuSfDnDamDOgFxCn50kfUawpWfXBToRogjYMD6LN8Jf9P6Bhb_fMNQp9OJlkL1BfBZb1LT5cPO0UO2m7THKDazs8cgGe__ulUE-LNljTHuvc5V3RvK2hzcLyXMs8cwRg5R5B3g-pxgao1mMyPeK7WtpF5ioCgchG7-H_bUWZA4qx9tmp--lEgfNiSqmxF6FBgKQBET-IV3X6sChQAWJ_7EBdGK7sweGNPViTNExVSAEusRl69fl2knL7-P0QEYV2L_-SBlBiUjECNbhTTeO2TDBGzOmoV953PTEeqJp1nAAAAATq1S1cA")
BOT_TOKEN = getenv("BOT_TOKEN", "5546240577:AAFc2H90K4Ebx2VqDJ41kT_QQE3cgb55IZ0")
BOT_NAME = getenv("BOT_NAME", "⌯ Lucifr music ༯")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "ᏒσŁＥχ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Too_9")
ALIVE_NAME = getenv("ALIVE_NAME", "ᏒσŁＥχ")
BOT_USERNAME = getenv("BOT_USERNAME", "Lu_cbot")
OWNER_ID = getenv("OWNER_ID", "5583171914")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "⌯ Lucifr music ༯")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "II_T2")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "II_T2")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5583171914").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
