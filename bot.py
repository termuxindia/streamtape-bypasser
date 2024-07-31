#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument

import os
from telegram.ext import ApplicationBuilder
from commands import command_handlers_list


BOT_TOKEN = os.environ.get(
    "BOT_TOKEN", "6308227197:AAHweeHPdwsa9SDWpr7g627qxpqtbZsaWsU"
)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    for handler in command_handlers_list:
        app.add_handler(handler)

    print("Started :)")

    app.run_polling()
