import sys
import asyncio
import logging
import traceback
import logging.handlers as handlers
from aiohttp import web
from pyrogram import idle
from BanOnExit.bot import app
from BanOnExit.server import web_server, keep_alive
from .configs import config
from pyrogram.enums import ChatMemberStatus


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%d/%m/%Y %H:%M:%S",
        format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(stream=sys.stdout),
            handlers.RotatingFileHandler(
                "app.log",
                mode="a",
                maxBytes=104857600,
                backupCount=2,
                encoding="utf-8",
            ),
        ],
    )
    logging.getLogger("aiohttp").setLevel(logging.ERROR)
    logging.getLogger("pyrogram").setLevel(logging.ERROR)
    logging.getLogger("aiohttp.web").setLevel(logging.ERROR)


async def start_services():
    try:
        logging.info("=========== Starting Server ===========")
        logging.info("=========== Initializing Telegram Bot ===========")
        await app.start()
        bot_info = await app.get_me()
        app.id = bot_info.id
        app.username = bot_info.username
        app.fname = bot_info.first_name
        logging.info("Telegram Bot Initialized Successfully")

        if config.KEEP_ALIVE:
            logging.info("=========== Starting Keep Alive Service ===========")
            asyncio.create_task(keep_alive())
            logging.info("Keep Alive Service Started")

        logging.info("=========== Initializing Web Server ===========")
        await server.setup()
        await web.TCPSite(server, config.BIND_ADDRESS, config.PORT).start()
        logging.info("Web Server Initialized Successfully")
        logging.info("=========== Service Startup Complete ===========")
        logging.info(f"Bot Name: {bot_info.first_name}")
        if bot_info.dc_id:
            logging.info(f"Bot Data Center ID: {bot_info.dc_id}")

        try:
            await on_bot_start()

        except:
            logging.info(f"Unable to contact admin after start")
        await idle()
    except Exception as e:
        logging.error(f"Error occurred during startup: {e}")
        traceback.print_exc()


async def cleanup():
    try:
        await server.cleanup()
        await app.stop()
    except Exception as e:
        logging.error(f"Error occurred during cleanup: {e}")


async def on_bot_start():
    await app.send_message(config.OWNER_ID, "Bot Started.. checking connected chats.")
    print("Bot Started.. checking connected chats.")

    # Iterate over each chat in the config
    for chat_id in config.CHATS:
        try:
            # Get the bot's current chat member status
            chat_member = await app.get_chat_member(chat_id, app.me.id)

            # Check if the bot has 'can_restrict_members' privilege
            if (
                chat_member.status == ChatMemberStatus.ADMINISTRATOR
                and chat_member.privileges.can_restrict_members
            ):
                print(
                    f"Bot has the 'can_restrict_members' privilege in chat {chat_id}. ✅"
                )
                await app.send_message(
                    config.OWNER_ID,
                    f"Bot has the 'can_restrict_members' privilege in chat {chat_id}. ✅",
                )

        except Exception as e:
            print(f"Error checking chat {chat_id}: {e}")
            await app.send_message(
                config.OWNER_ID,
                text=(
                    f"❌ Bot does NOT have the 'can_restrict_members' privilege in chat {chat_id}. "
                    f"Please make me admin as soon as possible so I can do my job effectively. 🙏"
                ),
            )
            print(
                f"❌ Bot does NOT have the 'can_restrict_members' privilege in chat {chat_id}. "
                f"Please make me admin as soon as possible so I can do my job effectively. 🙏"
            )


if __name__ == "__main__":
    setup_logging()
    server = web.AppRunner(web_server())
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(cleanup())
        loop.close()
        logging.info("=========== Stopped Services ===========")
