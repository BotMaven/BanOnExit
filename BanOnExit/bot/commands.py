import logging
from BanOnExit.bot import app
from BanOnExit.configs import config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters, Client


logger = logging.getLogger(__name__)


@app.on_message(filters.command(["start", "help"]))
async def start_command(app: Client, message: Message):

    if config.OWNER_ID == message.from_user.id:
        await message.reply_text(
            text=(
                f"**Welcome, {message.from_user.mention}! 👋 I'm always online to help keep things in check! ✅**\n\n"
                f"💡 **If anyone joins and leaves the chat within {config.BAN_THRESHOLD} seconds, I automatically remove them to maintain a quality environment. ⏳**"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="💡 Source Code 🌐",
                            url="https://github.com/BotMaven/BanOnExit",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
            quote=True,
        )
        return

    await message.reply_text(
        text=(
            "🚨 **This Bot is Privately Hosted** 🚨\n\n"
            "This bot is set up for personal use to automatically ban members after they leave a Group or Channel.\n"
            "If you'd like to use similar functionality, we encourage you to deploy your own instance.\n"
            "The full source code is open-source and readily available on GitHub for your convenience.\n\n"
            "🔗 **Get the Code Below:**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💡 Source Code 🌐",
                        url="https://github.com/BotMaven/BanOnExit",
                    )
                ]
            ]
        ),
        disable_web_page_preview=True,
        quote=True,
    )
