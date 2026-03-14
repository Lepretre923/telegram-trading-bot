import random
from market_data import crypto_price, get_history_tf
from indicator import calculate_rsi, calculate_macd, simple_moving_average, bollinger_bands

SCAN_ASSETS = ["BTC","ETH","SOL","BNB","XRP","ADA","DOGE","AVAX","MATIC"]
SEP = "━━━━━━━━━━━━━━"

# -------------------- Market Opportunity Scanner --------------------
def market_opportunity_scanner():
    results = []
    for asset in SCAN_ASSETS:
        price = crypto_price(asset)
        history = get_history_tf(asset, "1h")
        
        # Calcul indicateurs
        rsi = calculate_rsi(history) if history else 50
        macd_val, signal = calculate_macd(history) if history else (0,0)
        sma = simple_moving_average(history) if history else price
        mid, upper, lower = bollinger_bands(history) if history else (price, price*1.02, price*0.98)
        
        # Score simplifié basé sur momentum + RSI
        momentum = random.randint(-5,5)
        score = 50 + momentum*5
        if rsi > 60:
            score += 10
        elif rsi < 40:
            score -= 10
        results.append((asset, score, price))
    
    results.sort(key=lambda x:x[1], reverse=True)
    message = f"🚀 *SCANNER OPPORTUNITÉS*\n{SEP}\n"
    for asset, score, price in results[:5]:
        message += f"{asset}\nPrix: {price:.0f}$\nScore: {score}/100\n{SEP}\n"
    message += "\nGuide: Surveiller les actifs avec le score le plus élevé."
    return message

# -------------------- Whale Alert --------------------
def whale_radar():
    asset = random.choice(SCAN_ASSETS)
    volume = random.randint(500, 5000)
    movement = random.choice(["Accumulation possible","Distribution possible","Transfert entre portefeuilles"])
    impact = random.choice(["🟢 Impact haussier possible","🔴 Impact baissier possible","🟡 Impact neutre"])
    price = crypto_price(asset)
    
    return f"""
🐋 WHALE ALERT

Transaction détectée

Actif: {asset}
Volume: {volume}
Type mouvement: {movement}
Impact: {impact}
Prix actuel: {price:.0f}$
"""

# -------------------- Manipulation Radar --------------------
def manipulation_radar():
    asset = random.choice(SCAN_ASSETS)
    price = crypto_price(asset)
    trap = random.choice(["Possible fake breakout","Possible stop hunt","Zone manipulation probable","Marché stable"])
    risk = random.randint(10,90)
    danger = "🟡 Risque modéré"
    if risk > 70:
        danger = "🔴 Forte manipulation possible"
    elif risk < 30:
        danger = "🟢 Faible manipulation"
    return f"""
🧠 RADAR MANIPULATION

Actif: {asset}
Prix actuel: {price:.0f}$
Situation: {trap}
Risque: {danger}
Score: {risk}/100

Guide: Attendre confirmation avant entrée.
"""

# -------------------- Liquidation Radar --------------------
def liquidation_map():
    asset = random.choice(SCAN_ASSETS)
    price = crypto_price(asset)
    long_liq = price*0.95
    short_liq = price*1.05
    risk = random.randint(30,90)
    situation = "Neutre"
    if risk > 70:
        situation = "⚠️ Forte zone liquidation"
    elif risk < 40:
        situation = "🟢 Faible pression liquidation"
    return f"""
🔥 CARTE LIQUIDATIONS

Actif: {asset}
Prix actuel: {price:.0f}$

LONG: {long_liq:.0f}$
SHORT: {short_liq:.0f}$

Score risque: {risk}/100
Situation: {situation}

Guide: Les zones de liquidation attirent souvent le prix avant un retournement.
"""
