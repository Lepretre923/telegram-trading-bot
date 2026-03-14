import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from reports import full_report
from scanners import market_opportunity_scanner, liquidation_map, manipulation_radar
from alerts import btc_crash, whale_alert
from analysis import market_analysis, btc_chart
from signals import trading_signal
from intel import crypto_news
from market_data import crypto_price, metal_price, get_history_tf

TOKEN = "8764239542:AAFEkwls2LXhtSes1RyAT26i7LSKwnh0uGA"

# Flask pour Render
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_flask).start()

# Menu Telegram
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

# Commandes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot trading actif\n\nChoisis une analyse :",
        reply_markup=markup
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💰 BTC Analyse":
        await update.message.reply_text(btc_chart())
    elif text == "📋 Rapport complet":
        await update.message.reply_text(full_report())
    elif text == "🚨 Crash alert":
        await update.message.reply_text(btc_crash())
    elif text == "🐋 Whale alert":
        await update.message.reply_text(whale_alert())
    elif text == "📊 Score marché":
        await update.message.reply_text(market_analysis())
    elif text == "📈 Signal trading":
        await update.message.reply_text(trading_signal())
    elif text == "🧠 Analyse IA":
        await update.message.reply_text(crypto_news())
    elif text == "🔎 Scanner marché":
        await update.message.reply_text(market_opportunity_scanner())
    elif text == "🔥 Carte liquidations":
        await update.message.reply_text(liquidation_map())
    elif text == "🧠 Radar manipulation":
        await update.message.reply_text(manipulation_radar())
    # Ajouter les autres boutons ici

# Lancement bot
def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT, message))
    print("BOT ACTIF")
    app_bot.run_polling()

if __name__ == "__main__":
    main()
