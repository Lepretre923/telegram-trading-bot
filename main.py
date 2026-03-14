import os
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8764239542:AAFEkwls2LXhtSes1RyAT26i7LSKwnh0uGA"

# serveur pour Render
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running"

# commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot Telegram actif !")

# lancer le bot
async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("Bot lancé")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
