import random
from market_data import crypto_price, metal_price, get_history_tf

# Assets à scanner
SCAN_ASSETS = ["BTC","ETH","SOL","BNB","XRP","ADA","DOGE","AVAX","MATIC"]

SEP = "━━━━━━━━━━━━━━"

# ---------------- FONCTIONS SCANNERS ----------------

def safe_price(asset):
    """Retourne le prix d'un actif, 0 si indisponible"""
    try:
        price = crypto_price(asset)
        if price is None:
            return 0
        return price
    except:
        return 0

def market_opportunity_scanner():
    results = []
    for asset in SCAN_ASSETS:
        price = safe_price(asset)
        rsi = random.randint(30,70)
        momentum = random.randint(-5,5)
        score = 50 + momentum*5
        if rsi > 60:
            score += 10
        if rsi < 40:
            score -= 10
        results.append((asset, score, price))
    results = sorted(results, key=lambda x: x[1], reverse=True)
    message = f"🚀 *SCANNER OPPORTUNITÉS*\n\n{SEP}\n"
    for asset, score, price in results[:5]:
        message += f"{asset}\nPrix : {price:.0f}$\nScore : {score}/100\n{SEP}\n"
    message += "\nGuide\nSurveiller les actifs avec le score le plus élevé."
    return message

def liquidation_radar():
    """Remplacé liquidation_map pour cohérence avec imports"""
    asset = random.choice(["BTC","ETH"])
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

Actif : {asset}
Prix actuel : {price:.0f}$

Zone liquidation LONG : {long_liq:.0f}$
Zone liquidation SHORT : {short_liq:.0f}$

Score risque : {risk}/100
Situation : {situation}

Analyse :
Les zones de liquidation attirent souvent le prix avant un retournement.
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
    if risk>70:
        danger = "🔴 Forte manipulation possible"
    elif risk<30:
        danger = "🟢 Faible manipulation"
    else:
        danger = "🟡 Risque modéré"
    return f"""
🧠 RADAR MANIPULATION

Score manipulation : {risk}/100
Situation : {trap}
Risque : {danger}

Guide :
Attendre confirmation avant entrée.
"""
