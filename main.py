import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from alerts import btc_crash, whale_alert
from scanners import market_opportunity_scanner, liquidation_radar, manipulation_radar
from analysis import market_analysis, btc_chart
from signals import trading_signal
from reports import full_report
from intel import crypto_news
from market_data import crypto_price, metal_price, get_history_tf

TOKEN = "8764239542:AAFEkwls2LXhtSes1RyAT26i7LSKwnh0uGA"

# ---------------- FLASK ----------------
app = Flask(__name__)
@app.route("/")
def home():
    return "Bot running"
threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8080)).start()

# ---------------- TELEGRAM ----------------
keyboard = [["💰 BTC Analyse","🪙 ETH Analyse"],["☀️ SOL Analyse","🥇 GOLD Analyse"]]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot trading actif\nChoisis une analyse :", reply_markup=markup)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "💰 BTC Analyse":
        await update.message.reply_text(btc_chart())
    elif text == "📋 Rapport complet":
        await update.message.reply_text(full_report())

def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT, message))
    print("BOT ACTIF")
    app_bot.run_polling()

if __name__ == "__main__":
    main()
