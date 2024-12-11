from os import environ
from dotenv import load_dotenv

load_dotenv()


class config(object):
    API_ID = int(environ.get("API_ID"))
    API_HASH = str(environ.get("API_HASH"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD"))
    WORKERS = int(environ.get("WORKERS", "6"))
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "300"))
    URL = str(environ.get("URL"))
    CHATS = list(map(int, environ.get("CHATS").split(",")))
    OWNER_ID = int(environ.get("OWNER_ID", "6646387248"))
    KEEP_ALIVE = bool(environ.get("KEEP_ALIVE", False))
    BAN_THRESHOLD = int(environ.get("BAN_THRESHOLD", "60"))
