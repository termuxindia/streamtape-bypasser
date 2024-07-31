#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument,import-error
import os
from telegram import Update, constants
from telegram.ext import filters, CommandHandler, MessageHandler
from telegram.constants import ChatAction
from functools import wraps
from utils import get_streamtape_url


sudo_users_str = os.environ.get("SUDO_USERS", "5294965763")
SUDO_USERS = [int(i) for i in sudo_users_str.split(" ")]
user_filter = filters.User(user_id=SUDO_USERS)
html_mode = constants.ParseMode.HTML


Start_text = """Hello I'm Streamtape direct link generator."""


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        async def command_func(update, context, *args, **kwargs):
            await context.bot.send_chat_action(
                chat_id=update.effective_message.chat_id, action=action
            )
            return await func(update, context, *args, **kwargs)

        return command_func

    return decorator


@send_action(ChatAction.TYPING)
async def start_message(msg: Update, __):
    await msg.message.reply_text(Start_text, parse_mode=html_mode)


@send_action(ChatAction.TYPING)
async def streamtape_link_handler(msg: Update, __):
    try:
        link = msg.message.text.strip()
        direct_link = get_streamtape_url(link)
        text = f"Link: {link}\n\nDirect Link: {direct_link}\n\nCopy: <code>{direct_link}</code>"
        await msg.message.reply_text(text, parse_mode=html_mode)
    except:
        pass


start_handler = CommandHandler(
    ["start"], start_message, filters=user_filter & filters.ChatType.PRIVATE
)

STREAMTAPE_PATTERN = r"streamtape"
link_msg_handler = MessageHandler(
    callback=streamtape_link_handler,
    filters=filters.Regex(STREAMTAPE_PATTERN) & filters.ChatType.PRIVATE,
)


command_handlers_list = [start_handler, link_msg_handler]
