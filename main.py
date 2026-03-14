import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# IMPORTS MODULES
from reports import *
from scanners import *
from alerts import *
from market_data import *
from intel import *
from analysis import *

TOKEN = "8764239542:AAFEkwls2LXhtSes1RyAT26i7LSKwnh0uGA"


# ---------------- FLASK (RENDER KEEP ALIVE) ----------------

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running"


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
        "🤖 Trading AI Bot\n\nSelect an analysis:",
        reply_markup=markup
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text


    if text == "💰 BTC Analyse":
        await update.message.reply_text(btc_analysis())


    elif text == "🪙 ETH Analyse":
        await update.message.reply_text(analyse("ETH", crypto_price("ETH")))


    elif text == "☀️ SOL Analyse":
        await update.message.reply_text(analyse("SOL", crypto_price("SOL")))


    elif text == "🥇 GOLD Analyse":
        await update.message.reply_text(analyse("Gold", metal_price("XAU")))


    elif text == "🥈 SILVER Analyse":
        await update.message.reply_text(analyse("Silver", metal_price("XAG")))


    elif text == "🤖 Analyse IA":
        await update.message.reply_text(market_analysis())


    elif text == "📈 Signal trading":
        await update.message.reply_text(signal())


    elif text == "🚨 Crash alert":
        await update.message.reply_text(btc_crash())


    elif text == "🐋 Whale alert":
        await update.message.reply_text(whale_alert())


    elif text == "🔎 Scanner marché":
        await update.message.reply_text(scanner())


    elif text == "📡 Radar liquidité":
        await update.message.reply_text(liquidity())


    elif text == "🧠 Radar manipulation":
        await update.message.reply_text(manipulation_radar())


    elif text == "📊 Carte de trade":
        await update.message.reply_text(trade_map())


    elif text == "🧭 Carte institutionnelle":
        await update.message.reply_text(institutional())


    elif text == "🧮 Probabilité trade":
        await update.message.reply_text(probability())


    elif text == "📊 Score marché":
        await update.message.reply_text(market_score())


    elif text == "📊 Heatmap crypto":
        await update.message.reply_text(heatmap())


    elif text == "📡 Auto Watchlist":
        await update.message.reply_text(watchlist())


    elif text == "🧠 Analyse multi crypto":
        await update.message.reply_text(multi())


    elif text == "📆 Agenda économique":
        await update.message.reply_text(agenda())


    elif text == "🌅 Briefing marché":
        await update.message.reply_text(briefing())


    elif text == "📋 Rapport complet":
        await update.message.reply_text(report())


# ---------------- LANCEMENT BOT ----------------

def main():

    bot = ApplicationBuilder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.TEXT, message))

    print("BOT ACTIF")

    bot.run_polling()


if __name__ == "__main__":
    main()
