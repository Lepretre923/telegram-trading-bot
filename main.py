import asyncio
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# IMPORTS DE TES MODULES
from reports import (
    analyse, btc_analysis, signal, scanner, liquidity, trade_map,
    institutional, probability, multi_timeframe, market_score, ai,
    heatmap, watchlist, multi, agenda, briefing, report
)

from scanners import (
    liquidation_radar, macro_news, manipulation_radar, whale_radar,
    top_opportunities, market_sentiment, market_levels, market_pressure,
    top_movers, market_correlation, stop_hunt_radar, volatility_radar,
    crypto_market_index, market_opportunity_scanner, full_market_scan
)

from alerts import crash, whale

from market_data import (
    crypto_price, metal_price, fear_greed, funding_rate,
    open_interest, global_market
)

TOKEN = "8764239542:AAFEkwls2LXhtSes1RyAT26i7LSKwnh0uGA"


# -------- SERVEUR WEB POUR RENDER --------

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot running"


def run_web():
    app.run(host="0.0.0.0", port=8080)


Thread(target=run_web).start()


# -------- MENU TELEGRAM --------

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


# -------- COMMANDES --------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot trading actif\n\nChoisis une analyse :",
        reply_markup=markup
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    t = update.message.text

    if t == "💰 BTC Analyse":
        await update.message.reply_text(btc_analysis())

    elif t == "🪙 ETH Analyse":
        await update.message.reply_text(analyse("ETH", crypto_price("ETH")))

    elif t == "☀️ SOL Analyse":
        await update.message.reply_text(analyse("SOL", crypto_price("SOL")))

    elif t == "🥇 GOLD Analyse":
        await update.message.reply_text(analyse("Gold", metal_price("XAU")))

    elif t == "🥈 SILVER Analyse":
        await update.message.reply_text(analyse("Silver", metal_price("XAG")))

    elif t == "📈 Signal trading":
        await update.message.reply_text(signal())

    elif t == "🚨 Crash alert":
        await update.message.reply_text(crash())

    elif t == "🐋 Whale alert":
        await update.message.reply_text(whale())

    elif t == "🔎 Scanner marché":
        await update.message.reply_text(scanner())

    elif t == "📡 Radar liquidité":
        await update.message.reply_text(liquidity())

    elif t == "🧠 Radar manipulation":
        await update.message.reply_text(manipulation_radar())

    elif t == "📊 Carte de trade":
        await update.message.reply_text(trade_map())

    elif t == "🧭 Carte institutionnelle":
        await update.message.reply_text(institutional())

    elif t == "🧮 Probabilité trade":
        await update.message.reply_text(probability())

    elif t == "📊 Score marché":
        await update.message.reply_text(market_score())

    elif t == "📊 Heatmap crypto":
        await update.message.reply_text(heatmap())

    elif t == "📡 Auto Watchlist":
        await update.message.reply_text(watchlist())

    elif t == "🧠 Analyse multi crypto":
        await update.message.reply_text(multi())

    elif t == "📆 Agenda économique":
        await update.message.reply_text(agenda())

    elif t == "🌅 Briefing marché":
        await update.message.reply_text(briefing())

    elif t == "📋 Rapport complet":
        await update.message.reply_text(report())


# -------- LANCEMENT BOT --------

async def main():

    bot = ApplicationBuilder().token(TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(MessageHandler(filters.TEXT, message))

    print("BOT ACTIF")

    await bot.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
