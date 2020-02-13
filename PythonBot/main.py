#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def main():
    updater = Updater("", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, abiach))
    updater.start_polling()
    updater.idle()


def abiach(update, context):
    update.message.reply_text(update.message.text)


main()
