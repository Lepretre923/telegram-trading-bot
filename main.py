import threading
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ---- IMPORTS DES MODULES ----
from reports import full_report
from scanners import market_opportunity_scanner, liquidation_radar, manipulation_radar
from analysis import market_analysis, btc_chart
from alerts import btc_crash, whale_alert
from signals import trading_signal
from intel import crypto_news
from market_data import crypto_price, metal_price, get_history_tf

TOKEN = "TON_ANCIEN_TOKEN_ICI"  # Tu le remplaces par le nouveau

# ---- FLASK (Render Keep-Alive) ----
app = Flask(__name__)
@app.route("/")
def home():
    return "Bot running"

def run_flask():
    app.run(host="0.0.0.0", port=8080)
threading.Thread(target=run_flask).start()

# ---- MENU TELEGRAM ----
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

# ---- COMMANDES TELEGRAM ----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot trading actif\n\nChoisis une analyse :", reply_markup=markup)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # Tu ajoutes toutes tes commandes comme tu avais
    if text == "📋 Rapport complet":
        await update.message.reply_text(full_report())
    elif text == "💰 BTC Analyse":
        await update.message.reply_text(market_analysis())
    elif text == "🚨 Crash alert":
        await update.message.reply_text(btc_crash())
    elif text == "🐋 Whale alert":
        await update.message.reply_text(whale_alert())
    # Continue pour toutes les autres touches

# ---- LANCEMENT BOT ----
def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT, message))
    print("BOT ACTIF")
    app_bot.run_polling()

if __name__ == "__main__":
    main()
