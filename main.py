import os
import threading

from bot_modules import state
from bot_modules.config import DISCORD_TOKEN, MAIN_ADMIN_ID, logger
from bot_modules.bot_instance import bot
from bot_modules import database, core


def initialize():
    database.init_db()
    state.vps_data.clear()
    state.vps_data.update(database.get_vps_data())
    state.admin_data.clear()
    state.admin_data.update({"admins": database.get_admins()})
    state.CPU_THRESHOLD = int(database.get_setting("cpu_threshold", 90))
    state.RAM_THRESHOLD = int(database.get_setting("ram_threshold", 90))
    state.DEFAULT_STORAGE_POOL = os.getenv("DEFAULT_STORAGE_POOL") or core.get_default_storage_pool() or "default"


initialize()

from bot_modules import events  # noqa: E402,F401
from bot_modules import user_commands  # noqa: E402,F401
from bot_modules import vps_commands  # noqa: E402,F401
from bot_modules import admin_commands  # noqa: E402,F401
from bot_modules import node_commands  # noqa: E402,F401
from bot_modules import help_commands  # noqa: E402,F401

monitor_thread = threading.Thread(target=core.resource_monitor, daemon=True)
monitor_thread.start()


if __name__ == "__main__":
    if not DISCORD_TOKEN:
        logger.error("DISCORD_TOKEN is not set. Add it as an environment variable before starting the bot.")
        raise SystemExit(1)
    if not MAIN_ADMIN_ID:
        logger.error("MAIN_ADMIN_ID is not set. Add your Discord user ID before starting the bot.")
        raise SystemExit(1)
    bot.run(DISCORD_TOKEN)
