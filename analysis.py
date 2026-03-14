import random

def market_analysis():

    rsi = random.randint(30,70)

    macd = random.choice(["Bullish","Bearish"])

    sentiment = random.choice(["Bullish","Neutral","Bearish"])

    momentum = random.randint(-5,5)

    score = rsi

    if macd == "Bullish":
        score += 10
    else:
        score -= 10

    if sentiment == "Bullish":
        score += 10
    elif sentiment == "Bearish":
        score -= 10

    if momentum > 0:
        score += 5
    else:
        score -= 5

    if score > 100:
        score = 100

    if score < 0:
        score = 0


    trend = "Neutral"

    if score > 65:
        trend = "Bullish trend"

    if score < 40:
        trend = "Bearish trend"


    probability = random.randint(50,85)


    return f"""
📊 AI MARKET ANALYSIS

RSI
{rsi}

MACD
{macd}

Sentiment
{sentiment}

Momentum
{momentum}

━━━━━━━━━━━━━━

Market Score
{score}/100

Trend
{trend}

Probability
{probability} %

━━━━━━━━━━━━━━

Guide

Score > 65
Bullish market structure

Score 40 - 65
Neutral market

Score < 40
Bearish pressure
"""


def btc_chart():

    return """
📈 BTC CHART

TradingView

https://www.tradingview.com/chart/?symbol=BINANCE:BTCUSDT
"""
