import os

from telegram import Update

from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("LastZ Bot Aktif!")

app = Application.builder().token(TOKEN).build()

print("BOT BASLADI")

app.add_handler(CommandHandler("start", start))

app.run_polling()
