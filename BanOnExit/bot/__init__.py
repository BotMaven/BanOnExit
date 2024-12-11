from ..configs import config
from pyrogram import Client

app = Client(
    name="BanOnExit",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    workdir="BanOnExit",
    plugins={"root": "BanOnExit/bot"},
    bot_token=config.BOT_TOKEN,
    sleep_threshold=config.SLEEP_THRESHOLD,
    workers=config.WORKERS,
    no_updates=None,
)
