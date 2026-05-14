from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7801801985:AAHx4tHrDahkSnEYMHENCqFDvreXbAZ8Fv0"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("LastZ kod botu aktif!")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
