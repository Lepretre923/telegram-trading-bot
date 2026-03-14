import random
from market_data import crypto_price

SCAN_ASSETS = ["BTC","ETH","SOL","BNB","XRP","ADA","DOGE","AVAX","MATIC"]
SEP = "━━━━━━━━━━━━━━"

def market_opportunity_scanner():
    results = []
    for asset in SCAN_ASSETS:
        price = crypto_price(asset)
        rsi = random.randint(30,70)
        momentum = random.randint(-5,5)
        score = 50 + momentum*5
        if rsi > 60: score += 10
        if rsi < 40: score -= 10
        results.append((asset, score, price))
    results = sorted(results, key=lambda x: x[1], reverse=True)
    message = f"🚀 *SCANNER OPPORTUNITÉS*\n\n{SEP}\n"
    for asset, score, price in results[:5]:
        message += f"{asset}\nPrix : {price:.0f}$\nScore : {score}/100\n{SEP}\n"
    message += "\nGuide : Surveiller les actifs avec le score le plus élevé."
    return message

def liquidation_radar():
    btc = crypto_price("BTC")
    long_liq = btc * 0.96
    short_liq = btc * 1.04
    intensity = random.randint(30,90)
    cascade = random.choice([
        "Possible cascade liquidations longues",
        "Possible cascade liquidations shorts",
        "Liquidations faibles"
    ])
    return f"""
📉 RADAR LIQUIDATIONS
BTC : {btc:.0f}$
Zones liquidation longs : {long_liq:.0f}$
Zones liquidation shorts : {short_liq:.0f}$
Intensité : {intensity}%
Analyse : {cascade}
"""

def manipulation_radar():
    asset = random.choice(["BTC","ETH","SOL"])
    price = crypto_price(asset)
    trap = random.choice([
        "Possible fake breakout",
        "Possible stop hunt",
        "Zone manipulation probable",
        "Marché stable"
    ])
    risk = random.randint(10,90)
    risk_label = "Élevé" if risk > 70 else ("Faible" if risk < 30 else "Modéré")
    return f"""
🧠 RADAR MANIPULATION
Score manipulation : {risk}/100
Situation : {trap}
Risque : {risk_label}
Guide : Attendre confirmation avant entrée.
"""

def whale_radar():
    asset = random.choice(["BTC","ETH","SOL"])
    price = crypto_price(asset)
    volume = random.randint(1000,10000)
    movement = random.choice([
        "Accumulation possible",
        "Distribution possible",
        "Transfert entre portefeuilles"
    ])
    return f"""
🐋 WHALE ALERT
Transaction détectée : {volume} {asset}
Type mouvement : {movement}
Impact : Hausse de volatilité.
"""

def full_market_scan():
    btc = crypto_price("BTC")
    eth = crypto_price("ETH")
    sol = crypto_price("SOL")
    sentiment = random.randint(0,100)
    buy = random.randint(30,85)
    sell = random.randint(20,80)
    volatility = random.randint(3,10)
    dominant = random.choice(["BTC","ETH","SOL"])
    direction = "🟢 Marché haussier" if sentiment>65 else ("🔴 Marché baissier" if sentiment<40 else "Neutre")
    return f"""
🧭 SCANNER COMPLET DU MARCHÉ
BTC : {btc:.0f}$, ETH : {eth:.0f}$, SOL : {sol:.0f}$
Sentiment : {sentiment}/100
Pression : Acheteurs {buy}%, Vendeurs {sell}%
Volatilité : {volatility}%
Actif dominant : {dominant}
Direction : {direction}
Guide : Comparer sentiment, liquidité et momentum avant toute position.
"""
