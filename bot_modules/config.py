import logging
import os
from typing import List, Dict

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "").strip()
BOT_NAME = os.getenv("BOT_NAME", "INFINITE VPS BOT")
PREFIX = os.getenv("PREFIX", "!")
YOUR_SERVER_IP = os.getenv("YOUR_SERVER_IP", "127.0.0.1")
MAIN_ADMIN_ID = int(os.getenv("MAIN_ADMIN_ID", "0"))
BOT_VERSION = os.getenv("BOT_VERSION", "7.0-PRO")
BOT_DEVELOPER = os.getenv("BOT_DEVELOPER", "INFINITE")

OS_OPTIONS: List[Dict[str, str]] = [
    {"label": "Ubuntu 20.04 LTS", "value": "ubuntu:20.04"},
    {"label": "Ubuntu 22.04 LTS", "value": "ubuntu:22.04"},
    {"label": "Ubuntu 24.04 LTS", "value": "ubuntu:24.04"},
    {"label": "Debian 10 (Buster)", "value": "images:debian/10"},
    {"label": "Debian 11 (Bullseye)", "value": "images:debian/11"},
    {"label": "Debian 12 (Bookworm)", "value": "images:debian/12"},
    {"label": "Debian 13 (Trixie)", "value": "images:debian/13"},
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
logger = logging.getLogger(f"{BOT_NAME.lower().replace(' ', '_')}_vps_bot")
