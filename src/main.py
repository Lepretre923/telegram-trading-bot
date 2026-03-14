import os
import datetime
from flask import Flask
from threading import Thread
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from market_data import crypto_price, metal_price, fear_greed, funding_rate, open_interest, global_market
from indicators import calculate_rsi, moving_average
from reports import (
    analyse, btc_analysis, signal, scanner, liquidity, trade_map,
    institutional, probability, multi_timeframe, market_score, ai,
    heatmap, watchlist, multi, agenda, briefing, report,
    market_dashboard, super_report, trading_assistant
)
from scanners import (
    liquidation_radar, macro_news, manipulation_radar, whale_radar,
    top_opportunities, market_sentiment, market_levels, market_pressure,
    top_movers, market_correlation, stop_hunt_radar, volatility_radar,
    crypto_market_index, opportunity_scanner, full_market_scan,
    market_opportunity_scanner, liquidation_map, volume_profile, stablecoin_flow
)
from alerts import (
    crash, whale,
    market_alert, auto_market_report, opportunity_alert,
    breakout_alert, daily_report, daily_trade_plan, danger_alert
)

flaskapp=Flask(__name__)

@flaskapp.route('/')
def home():
    return "Bot running"

def run_flask():
    flaskapp.run(host="0.0.0.0",port=8080)

Thread(target=run_flask).start()

TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")

keyboard=[
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
["🌅 Briefing marché","📋 Rapport complet"],
["⏱ Multi timeframe","📉 Radar liquidations"],
["📰 News macro","🗺 Niveaux marché"],
["📊 Sentiment marché","🏆 Top opportunités"],
["🐋 Whale radar","🧠 Manipulation radar"],
["📊 Pression marché","🔥 Top movers"],
["📊 Corrélation marché","🎯 Radar stop hunt"],
["🧠 Super rapport IA","🤖 Assistant trading"],
["📊 Dashboard marché","🧭 Scanner complet"],
["🚀 Scanner opportunités","🌐 Indice global crypto"],
["⚡ Radar volatilité"],
["📊 Graphique BTC","📊 Graphique ETH"],
["📊 Fear & Greed","📉 Funding rate"],
["📊 Open interest","🔥 Liquidation map"],
["📊 Volume profile","💵 Stablecoin flow"],
["🌍 Marché global"]
]

markup=ReplyKeyboardMarkup(keyboard,resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot actif",reply_markup=markup)
    context.job_queue.run_repeating(market_alert,interval=300,first=60,chat_id=update.effective_chat.id)
    context.job_queue.run_repeating(auto_market_report,interval=7200,first=60,chat_id=update.effective_chat.id)
    context.job_queue.run_daily(daily_trade_plan,time=datetime.time(hour=7,minute=30),chat_id=update.effective_chat.id)
    context.job_queue.run_daily(daily_report,time=datetime.time(hour=8,minute=0),chat_id=update.effective_chat.id)
    context.job_queue.run_daily(daily_report,time=datetime.time(hour=13,minute=0),chat_id=update.effective_chat.id)
    context.job_queue.run_daily(daily_report,time=datetime.time(hour=20,minute=0),chat_id=update.effective_chat.id)
    context.job_queue.run_repeating(danger_alert,interval=300,first=60,chat_id=update.effective_chat.id)
    context.job_queue.run_repeating(opportunity_alert,interval=600,first=60,chat_id=update.effective_chat.id)
    context.job_queue.run_repeating(breakout_alert,interval=900,first=60,chat_id=update.effective_chat.id)

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t=update.message.text

    pm="Markdown"

    if t=="💰 BTC Analyse":
        await update.message.reply_text(btc_analysis(),parse_mode=pm)
    elif t=="🪙 ETH Analyse":
        await update.message.reply_text(analyse("ETH",crypto_price("ETH")),parse_mode=pm)
    elif t=="☀️ SOL Analyse":
        await update.message.reply_text(analyse("SOL",crypto_price("SOL")),parse_mode=pm)
    elif t=="🥇 GOLD Analyse":
        await update.message.reply_text(analyse("Gold",metal_price("XAU")),parse_mode=pm)
    elif t=="🥈 SILVER Analyse":
        await update.message.reply_text(analyse("Silver",metal_price("XAG")),parse_mode=pm)
    elif t=="📈 Signal trading":
        await update.message.reply_text(signal(),parse_mode=pm)
    elif t=="🚨 Crash alert":
        await update.message.reply_text(crash(),parse_mode=pm)
    elif t=="🐋 Whale alert":
        await update.message.reply_text(whale_radar(),parse_mode=pm)
    elif t=="🔎 Scanner marché":
        await update.message.reply_text(scanner(),parse_mode=pm)
    elif t=="📡 Radar liquidité":
        await update.message.reply_text(liquidity(),parse_mode=pm)
    elif t=="🧠 Radar manipulation" or t=="🧠 Manipulation radar":
        await update.message.reply_text(manipulation_radar(),parse_mode=pm)
    elif t=="📊 Pression marché":
        await update.message.reply_text(market_pressure(),parse_mode=pm)
    elif t=="🔥 Top movers":
        await update.message.reply_text(top_movers(),parse_mode=pm)
    elif t=="📊 Corrélation marché":
        await update.message.reply_text(market_correlation(),parse_mode=pm)
    elif t=="🎯 Radar stop hunt" or t=="🎯 Stop hunt radar":
        await update.message.reply_text(stop_hunt_radar(),parse_mode=pm)
    elif t=="🧠 Super rapport IA":
        await update.message.reply_text(super_report(),parse_mode=pm)
    elif t=="🤖 Assistant trading":
        await update.message.reply_text(trading_assistant(),parse_mode=pm)
    elif t=="📊 Dashboard marché":
        await update.message.reply_text(market_dashboard(),parse_mode=pm)
    elif t=="🧭 Scanner complet":
        await update.message.reply_text(full_market_scan(),parse_mode=pm)
    elif t=="🚀 Scanner opportunités":
        await update.message.reply_text(market_opportunity_scanner(),parse_mode=pm)
    elif t=="🌐 Indice global crypto" or t=="🌐 Indice marché crypto":
        await update.message.reply_text(crypto_market_index(),parse_mode=pm)
    elif t=="⚡ Radar volatilité":
        await update.message.reply_text(volatility_radar(),parse_mode=pm)
    elif t=="📉 Radar liquidations":
        await update.message.reply_text(liquidation_radar(),parse_mode=pm)
    elif t=="📰 News macro":
        await update.message.reply_text(macro_news(),parse_mode=pm)
    elif t=="🗺 Niveaux marché":
        await update.message.reply_text(market_levels(),parse_mode=pm)
    elif t=="📊 Sentiment marché":
        await update.message.reply_text(market_sentiment(),parse_mode=pm)
    elif t=="🏆 Top opportunités":
        await update.message.reply_text(top_opportunities(),parse_mode=pm)
    elif t=="🐋 Whale radar":
        await update.message.reply_text(whale_radar(),parse_mode=pm)
    elif t=="📊 Carte de trade":
        await update.message.reply_text(trade_map(),parse_mode=pm)
    elif t=="🧭 Carte institutionnelle":
        await update.message.reply_text(institutional(),parse_mode=pm)
    elif t=="🧮 Probabilité trade":
        await update.message.reply_text(probability(),parse_mode=pm)
    elif t=="🤖 Analyse IA":
        await update.message.reply_text(trading_assistant(),parse_mode=pm)
    elif t=="📊 Score marché":
        await update.message.reply_text(market_score(),parse_mode=pm)
    elif t=="📊 Heatmap crypto":
        await update.message.reply_text(heatmap(),parse_mode=pm)
    elif t=="📡 Auto Watchlist":
        await update.message.reply_text(watchlist(),parse_mode=pm)
    elif t=="🧠 Analyse multi crypto":
        await update.message.reply_text(multi(),parse_mode=pm)
    elif t=="📆 Agenda économique":
        await update.message.reply_text(agenda(),parse_mode=pm)
    elif t=="🌅 Briefing marché":
        await update.message.reply_text(briefing(),parse_mode=pm)
    elif t=="📋 Rapport complet":
        await update.message.reply_text(report(),parse_mode=pm)
    elif t=="⏱ Multi timeframe":
        await update.message.reply_text(multi_timeframe("BTC"),parse_mode=pm)
    elif t=="📊 Graphique BTC":
        await update.message.reply_photo(
            photo="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT",
            caption="📊 Graphique BTC"
        )
    elif t=="📊 Graphique ETH":
        await update.message.reply_photo(
            photo="https://s.tradingview.com/widgetembed/?symbol=BINANCE:ETHUSDT",
            caption="📊 Graphique ETH"
        )
    elif t=="📊 Fear & Greed":
        await update.message.reply_text(fear_greed(),parse_mode="Markdown")
    elif t=="📉 Funding rate":
        await update.message.reply_text(funding_rate(),parse_mode="Markdown")
    elif t=="📊 Open interest":
        await update.message.reply_text(open_interest(),parse_mode="Markdown")
    elif t=="🔥 Liquidation map":
        await update.message.reply_text(liquidation_map(),parse_mode="Markdown")
    elif t=="📊 Volume profile":
        await update.message.reply_text(volume_profile(),parse_mode="Markdown")
    elif t=="💵 Stablecoin flow":
        await update.message.reply_text(stablecoin_flow(),parse_mode="Markdown")
    elif t=="🌍 Marché global":
        await update.message.reply_text(global_market(),parse_mode="Markdown")

app=ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT,message))

print("BOT ACTIF")

app.run_polling()
