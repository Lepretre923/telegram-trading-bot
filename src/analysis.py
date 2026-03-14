import random

def analyse(symbol="BTC"):

    rsi=random.randint(20,80)

    macd=random.choice(["bullish","bearish"])

    sentiment=random.choice(["haussier","neutre","baissier"])

    score=rsi

    if macd=="bullish":
        score+=10
    else:
        score-=10

    return f"""
📊 Analyse marché

Crypto : {symbol}

RSI : {rsi}
MACD : {macd}
Sentiment : {sentiment}

Score marché : {score}/100
"""


def multi_indicators(symbol="BTC"):

    rsi=random.randint(20,80)

    macd=random.choice(["bullish","bearish"])

    volume=random.choice(["élevé","moyen","faible"])

    trend=random.choice(["haussier","baissier","neutre"])

    return f"""
📊 Analyse avancée

Crypto : {symbol}

RSI : {rsi}
MACD : {macd}
Volume : {volume}
Trend : {trend}
"""


def trade_score():

    probability=random.randint(50,95)

    return f"""
🤖 Score IA du trade

Probabilité de réussite :

{probability} %
"""