import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
                                                                                                              TOKEN = os.getenv("TOKEN")
TOKEN = os.getenv("TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("LastZ kod botu aktif!")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
