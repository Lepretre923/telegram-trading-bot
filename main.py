import asyncio
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

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
        msg = """
💰 ANALYSE BTC

Structure marché
Support : 67000 $
Résistance : 70500 $

RSI : 61
Momentum : +3
Volatilité : 6 %

Tendance
Haussière court terme

Guide
Attendre retour sur support avant entrée.
"""
        await update.message.reply_text(msg)

    elif t == "🪙 ETH Analyse":
        await update.message.reply_text("Analyse ETH en cours...")

    elif t == "☀️ SOL Analyse":
        await update.message.reply_text("Analyse SOL en cours...")

    elif t == "🥇 GOLD Analyse":
        await update.message.reply_text("Analyse Gold en cours...")

    elif t == "🥈 SILVER Analyse":
        await update.message.reply_text("Analyse Silver en cours...")

    elif t == "📈 Signal trading":
        await update.message.reply_text(
            "📈 Signal détecté\n\nEntrée : attendre confirmation tendance."
        )

    elif t == "🚨 Crash alert":
        await update.message.reply_text(
            "🚨 Risque de correction détecté.\n\nSurveiller supports majeurs."
        )

    elif t == "🐋 Whale alert":
        await update.message.reply_text(
            "🐋 Mouvement whale détecté.\nVolatilité possible."
        )

    elif t == "🔎 Scanner marché":
        await update.message.reply_text(
            "🔎 Analyse du marché en cours..."
        )

    elif t == "📡 Radar liquidité":
        await update.message.reply_text(
            "📡 Zones de liquidité détectées autour des niveaux clés."
        )

    elif t == "🧠 Radar manipulation":
        await update.message.reply_text(
            "🧠 Risque manipulation : modéré."
        )

    elif t == "📊 Carte de trade":
        await update.message.reply_text(
            "📊 Carte de trade générée."
        )

    elif t == "🧭 Carte institutionnelle":
        await update.message.reply_text(
            "🧭 Flux institutionnels analysés."
        )

    elif t == "🧮 Probabilité trade":
        await update.message.reply_text(
            "🧮 Probabilité du setup : 67%"
        )

    elif t == "📊 Score marché":
        await update.message.reply_text(
            "📊 Score marché global : 62/100"
        )

    elif t == "📊 Heatmap crypto":
        await update.message.reply_text(
            "📊 Heatmap crypto analysée."
        )

    elif t == "📡 Auto Watchlist":
        await update.message.reply_text(
            "📡 Actifs à surveiller : BTC / ETH / SOL"
        )

    elif t == "🧠 Analyse multi crypto":
        await update.message.reply_text(
            "🧠 Analyse multi crypto en cours."
        )

    elif t == "📆 Agenda économique":
        await update.message.reply_text(
            "📆 Agenda économique\nhttps://www.forexfactory.com/calendar"
        )

    elif t == "🌅 Briefing marché":
        await update.message.reply_text(
            "🌅 Briefing marché : volatilité modérée."
        )

    elif t == "📋 Rapport complet":
        await update.message.reply_text(
            "📋 Rapport complet généré."
        )

# -------- LANCEMENT BOT --------

async def main():

    app_bot = ApplicationBuilder().token(TOKEN).build()

    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT, message))

    print("BOT ACTIF")

    await app_bot.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
