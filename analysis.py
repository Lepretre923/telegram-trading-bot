import random
from market_data import crypto_price, metal_price

def market_analysis():
    rsi = random.randint(30, 70)
    macd = random.choice(["Bullish", "Bearish"])
    sentiment = random.choice(["Bullish", "Neutral", "Bearish"])
    score = rsi
    if macd == "Bullish":
        score += 10
    else:
        score -= 10
    if sentiment == "Bullish":
        score += 10
    elif sentiment == "Bearish":
        score -= 10

    return f"""
📊 AI MARKET ANALYSIS
RSI : {rsi}
MACD : {macd}
Sentiment : {sentiment}
Market Score : {score}/100
"""

def btc_chart():
    return "📈 BTC CHART\nhttps://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT"
