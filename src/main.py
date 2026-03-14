# main.py
import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# --- IMPORT DES MODULES ---
from alerts import btc_crash, whale_alert
from scanners import market_opportunity_scanner, liquidation_radar, manipulation_radar
from analysis import market_analysis, btc_chart
from signals import trading_signal
from reports import full_report
from intel import crypto_news
from market_data import crypto_price, metal_price, get_history_tf
from indicator import calculate_rsi, moving_average, macd, bollinger_bands, generate_random_indicator_signal

# --- TOKEN BOT ---
TOKEN = "8764239542:AAFEkwls2LXhtSes1RyAT26i7LSKwnh0uGA"

# ---------------- FLASK ----------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask).start()

# ---------------- MENU TELEGRAM ----------------
keyboard = [
    ["💰 BTC Analyse","🪙 ETH Analyse"],
    ["☀️ SOL Analyse","🥇 GOLD Analyse"],
    ["🥈 SILVER Analyse","🤖 Analyse IA"],
    ["📈 Signal trading","🚨 Crash alert"],
    ["🐋 Whale alert","🔎 Scanner marché"],
    ["📡 Radar liquidité","🧠 Radar manipulation"],
    ["📊 Carte de trade","🧭 Carte institutionnelle"],
    ["🧮 Probabilité trade","📊 Score marché"],
    ["📊 Heatmap crypto","📡 Auto Watchlist"],
    ["🧠 Analyse multi crypto","📆 Agenda économique"],
    ["🌅 Briefing marché","📋 Rapport complet"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ---------------- COMMANDES ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot trading actif\n\nChoisis une analyse :",
        reply_markup=markup
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # --- ALERTS ---
    if text == "🚨 Crash alert":
        await update.message.reply_text(btc_crash())
    elif text == "🐋 Whale alert":
        await update.message.reply_text(whale_alert())

    # --- ANALYSES ---
    elif text == "💰 BTC Analyse":
        await update.message.reply_text(market_analysis())
    elif text == "📊 Score marché":
        await update.message.reply_text(market_analysis())
    elif text == "🤖 Analyse IA":
        await update.message.reply_text(generate_random_indicator_signal())

    # --- SIGNALS ---
    elif text == "📈 Signal trading":
        await update.message.reply_text(trading_signal())

    # --- SCANNERS ---
    elif text == "🔎 Scanner marché":
        await update.message.reply_text(market_opportunity_scanner())
    elif text == "📡 Radar liquidité":
        await update.message.reply_text(liquidation_radar())
    elif text == "🧠 Radar manipulation":
        await update.message.reply_text(manipulation_radar())

    # --- REPORTS & NEWS ---
    elif text == "📋 Rapport complet":
        await update.message.reply_text(full_report())
    elif text == "📰 Crypto News":
        await update.message.reply_text(crypto_news())

# ---------------- LANCEMENT BOT ----------------
def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT, message))
    print("BOT ACTIF")
    app_bot.run_polling()

