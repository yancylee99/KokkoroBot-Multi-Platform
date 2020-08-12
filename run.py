import kokkoro
from kokkoro import config

import asyncio
import threading

kkr_bot = kokkoro.get_bot()
quart_app = kokkoro.get_app()

from kokkoro import web

if config.BOT_TYPE != "wechat_enterprise":
    def run_quart():
        quart_app.run("0.0.0.0", 5001, debug=True)
    thread = threading.Thread(target=run_quart)
    thread.start()

kkr_bot.kkr_run()
