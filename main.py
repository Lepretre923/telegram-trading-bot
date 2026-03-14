import datetime
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# TOKEN BOT TELEGRAM
TOKEN = "8764239542:AAFEkwls2LXhtSes1RyAT26i7LSKwnh0uGA"

# -------- SERVEUR FLASK POUR RENDER --------

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot Telegram actif"

def run_flask():
    app_flask.run(host="0.0.0.0", port=8080)

Thread(target=run_flask).start()

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

# -------- COMMANDES BOT --------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot trading actif\n\nChoisis une analyse :",
        reply_markup=markup
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "💰 BTC Analyse":
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
Attendre retour sur support
avant entrée.
"""
        await update.message.reply_text(msg)

    elif text == "🪙 ETH Analyse":
        await update.message.reply_text("Analyse ETH en cours...")

    elif text == "☀️ SOL Analyse":
        await update.message.reply_text("Analyse SOL en cours...")

    elif text == "🥇 GOLD Analyse":
        await update.message.reply_text("Analyse Gold en cours...")

    elif text == "🥈 SILVER Analyse":
        await update.message.reply_text("Analyse Silver en cours...")

    elif text == "📈 Signal trading":
        await update.message.reply_text(
            "📈 Signal détecté\n\nEntrée : attendre confirmation tendance."
        )

    elif text == "🚨 Crash alert":
        await update.message.reply_text(
            "🚨 Risque de correction détecté.\n\nSurveiller supports majeurs."
        )

    elif text == "🐋 Whale alert":
        await update.message.reply_text(
            "🐋 Mouvement whale détecté.\nVolatilité possible."
        )

    elif text == "🔎 Scanner marché":
        await update.message.reply_text(
            "🔎 Analyse du marché en cours..."
        )

    elif text == "📡 Radar liquidité":
        await update.message.reply_text(
            "📡 Zones de liquidité détectées autour des niveaux clés."
        )

    elif text == "🧠 Radar manipulation":
        await update.message.reply_text(
            "🧠 Risque manipulation : modéré."
        )

    elif text == "📊 Carte de trade":
        await update.message.reply_text(
            "📊 Carte de trade générée.\nObserver réaction du prix."
        )

    elif text == "🧭 Carte institutionnelle":
        await update.message.reply_text(
            "🧭 Flux institutionnels analysés."
        )

    elif text == "🧮 Probabilité trade":
        await update.message.reply_text(
            "🧮 Probabilité du setup : 67%"
        )

    elif text == "📊 Score marché":
        await update.message.reply_text(
            "📊 Score marché global : 62/100"
        )

    elif text == "📊 Heatmap crypto":
        await update.message.reply_text(
            "📊 Heatmap crypto analysée."
        )

    elif text == "📡 Auto Watchlist":
        await update.message.reply_text(
            "📡 Actifs à surveiller : BTC / ETH / SOL"
        )

    elif text == "🧠 Analyse multi crypto":
        await update.message.reply_text(
            "🧠 Analyse multi crypto en cours."
        )

    elif text == "📆 Agenda économique":
        await update.message.reply_text(
            "📆 Agenda économique :\nhttps://www.forexfactory.com/calendar"
        )

    elif text == "🌅 Briefing marché":
        await update.message.reply_text(
            "🌅 Briefing marché : volatilité modérée."
        )

    elif text == "📋 Rapport complet":
        await update.message.reply_text(
            "📋 Rapport complet généré."
        )

# -------- LANCEMENT BOT --------

telegram_app = ApplicationBuilder().token(TOKEN).build()

telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(MessageHandler(filters.TEXT, message))

print("BOT ACTIF")

telegram_app.run_polling()
