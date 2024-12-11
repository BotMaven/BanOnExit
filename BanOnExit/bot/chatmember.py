
import logging
from BanOnExit.bot import app
from pyrogram.types import ChatMemberUpdated
from pyrogram import Client
from pyrogram.enums import ChatType
from BanOnExit.configs import config
from datetime import datetime

logger = logging.getLogger(__name__)


@app.on_chat_member_updated()
async def handle_chat_member_update(app: Client, m: ChatMemberUpdated):
    chat = m.chat
    if chat.type in (ChatType.SUPERGROUP, ChatType.CHANNEL) and chat.id in config.CHATS:
        # Check if it's a user leave event
        m.new_chat_member.privileges.can_restrict_members
        if m.old_chat_member and not m.old_chat_member.user.is_self:
            user = m.old_chat_member.user
            joined_date = m.old_chat_member.joined_date  # When the user joined
            current_time = datetime.utcnow()  # Current UTC time

            # Calculate the time spent in the chat
            time_spent_in_chat = (current_time - joined_date).total_seconds()

            print(
                f"User {user.first_name} ({user.id}) left {chat.type.name} '{chat.title}' (ID: {chat.id}) at {joined_date}"
            )

            # Check if the user joined within the ban threshold (60 seconds)
            if time_spent_in_chat < config.BAN_THRESHOLD:
                print(
                    f"Banning user {user.first_name} ({user.id}) for leaving too soon."
                )

                # Ban the user
                await app.ban_chat_member(chat.id, user.id)
                print(
                    f"User {user.first_name} banned for leaving within {config.BAN_THRESHOLD} seconds."
                )
