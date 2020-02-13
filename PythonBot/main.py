#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def main():
    updater = Updater("967478626:AAESd8Cyt84ISkPsHl5D3qculg5zlkr6NGU", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, abiach))
    updater.start_polling()
    updater.idle()


def abiach(update, context):
    update.message.reply_text(update.message.text)


main()
