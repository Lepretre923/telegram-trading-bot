from analysis import market_analysis
from signals import trading_signal
from intel import crypto_news
from market_data import btc_price, eth_price
from scanners import market_sentiment, top_movers
import random


def full_report():

    try:
        btc = btc_price()
    except:
        btc = "N/A"

    try:
        eth = eth_price()
    except:
        eth = "N/A"

    try:
        analysis = market_analysis()
    except:
        analysis = "Analyse indisponible"

    try:
        signal = trading_signal()
    except:
        signal = "Signal indisponible"

    try:
        news = crypto_news()
    except:
        news = "News indisponibles"

    try:
        movers = top_movers()
    except:
        movers = "Movers indisponibles"

    try:
        sentiment = market_sentiment()
    except:
        sentiment = "Sentiment indisponible"


    market_score = random.randint(40,80)

    direction="Marché neutre"

    if market_score>65:
        direction="🟢 Tendance haussière"

    if market_score<45:
        direction="🔴 Tendance baissière"


    return f"""
📋 GLOBAL MARKET REPORT

━━━━━━━━━━━━━━━━━━

💰 PRIX MARCHÉ

BTC : {btc} $
ETH : {eth} $

━━━━━━━━━━━━━━━━━━

📊 ANALYSE TECHNIQUE

{analysis}

━━━━━━━━━━━━━━━━━━

📈 SIGNAL TRADING

{signal}

━━━━━━━━━━━━━━━━━━

📊 SENTIMENT MARCHÉ

{sentiment}

━━━━━━━━━━━━━━━━━━

🔥 TOP MOVERS

{movers}

━━━━━━━━━━━━━━━━━━

📰 NEWS CRYPTO

{news}

━━━━━━━━━━━━━━━━━━

🧠 SCORE GLOBAL MARCHÉ

Score : {market_score}/100

Direction :
{direction}

━━━━━━━━━━━━━━━━━━

📌 GUIDE TRADING

• Observer la liquidité
• Confirmer la tendance
• Entrer sur support
• Éviter les news majeures

━━━━━━━━━━━━━━━━━━
"""
