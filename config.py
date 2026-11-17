import os
from dotenv import load_dotenv

load_dotenv()

def required(name):
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"{name} belum diatur di file .env")
    return value

API_ID = int(required("API_ID"))
API_HASH = required("API_HASH")
BOT_TOKEN = required("BOT_TOKEN")
DO_TOKEN = required("DO_TOKEN")

OWNER_IDS = {
    int(value.strip())
    for value in os.getenv("OWNER_IDS", "").split(",")
    if value.strip().isdigit()
}

DO_SSH_KEY_IDS = [
    int(value.strip())
    for value in os.getenv("DO_SSH_KEY_IDS", "").split(",")
    if value.strip().isdigit()
]

MAX_MANAGED_DROPLETS = max(1, int(os.getenv("MAX_MANAGED_DROPLETS", "1")))
DO_IMAGE = os.getenv("DO_IMAGE", "ubuntu-24-04-x64").strip()
DO_TAG = os.getenv("DO_TAG", "managed-by-telegram-bot").strip()
