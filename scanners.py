import random
from market_data import crypto_price, metal_price, get_history_tf

SCAN_ASSETS = [
    "BTC","ETH","SOL","BNB","XRP",
    "ADA","DOGE","AVAX","MATIC"
]

SEP = "━━━━━━━━━━━━━━"

# ---------------- FONCTION SÛRE DE PRIX ----------------
def safe_price(asset):
    try:
        price = crypto_price(asset)
        return price if price else 0
    except:
        return 0

# ---------------- SCANNER D’OPPORTUNITÉS ----------------
def market_opportunity_scanner():
    results = []
    for asset in SCAN_ASSETS:
        price = safe_price(asset)
        rsi = random.randint(30,70)
        momentum = random.randint(-5,5)
        score = 50 + momentum*5
        if rsi > 60: score += 10
        if rsi < 40: score -= 10
        results.append((asset, score, price))

    results = sorted(results, key=lambda x: x[1], reverse=True)
    message = f"🚀 *SCANNER OPPORTUNITÉS*\n\n{SEP}\n"
    for asset, score, price in results[:5]:
        message += f"""
{asset}
Prix : {price:.0f}$
Score : {score}/100
{SEP}
"""
    message += "\nGuide : Surveiller les actifs avec le score le plus élevé."
    return message

# ---------------- FLOW STABLECOINS ----------------
def stablecoin_flow():
    inflow = random.randint(100,900)
    outflow = random.randint(100,900)
    net = inflow - outflow
    situation = "Neutre"
    if net > 200: situation = "🟢 Entrée de capitaux"
    elif net < -200: situation = "🔴 Sortie de capitaux"
    sign = "+" if net >= 0 else ""
    return f"""
💵 STABLECOIN FLOW
Entrées : {inflow} M$
Sorties : {outflow} M$
Flux net : {sign}{net} M$
Situation : {situation}
"""

# ---------------- VOLUME PROFILE ----------------
def volume_profile():
    asset = random.choice(["BTC","ETH"])
    price = safe_price(asset)
    poc = price * 0.99
    high_volume = price * 1.01
    low_volume = price * 0.97
    activity = random.randint(40,90)
    situation = "Volume équilibré"
    if activity > 70: situation = "📈 Forte activité marché"
    elif activity < 50: situation = "📉 Faible activité"
    return f"""
📊 VOLUME PROFILE
{asset}
Prix : {price:.0f}$
Point of Control : {poc:.0f}$
High Volume Zone : {high_volume:.0f}$
Low Volume Zone : {low_volume:.0f}$
Activité marché : {activity}
Situation : {situation}
"""

# ---------------- CARTE LIQUIDATIONS ----------------
def liquidation_map():
    asset = random.choice(["BTC","ETH"])
    price = safe_price(asset)
    long_liq = price * 0.95
    short_liq = price * 1.05
    risk = random.randint(30,90)
    situation = "Neutre"
    if risk > 70: situation = "⚠️ Forte zone liquidation"
    elif risk < 40: situation = "🟢 Faible pression liquidation"
    return f"""
🔥 CARTE LIQUIDATIONS
Actif : {asset}
Prix actuel : {price:.0f}$
━━━━━━━━━━━━━━
Zone liquidation LONG : {long_liq:.0f}$
Zone liquidation SHORT : {short_liq:.0f}$
━━━━━━━━━━━━━━
Score risque : {risk}/100
Situation : {situation}
━━━━━━━━━━━━━━
Analyse : Les zones de liquidation attirent souvent le prix avant un retournement.
"""

# ---------------- RADAR WHALE ----------------
def whale_radar():
    asset = random.choice(["BTC","ETH","SOL"])
    price = safe_price(asset)
    volume = random.randint(1000,10000)
    movement = random.choice([
        "Accumulation possible",
        "Distribution possible",
        "Transfert entre portefeuilles"
    ])
    impact = random.choice([
        "🟢 Impact haussier possible",
        "🔴 Impact baissier possible",
        "🟡 Impact neutre"
    ])
    return f"""
🐋 WHALE ALERT
Transaction détectée : {volume} {asset}
Type mouvement : {movement}
Impact : {impact}
"""

# ---------------- RADAR VOLATILITÉ ----------------
def volatility_radar():
    asset = random.choice(["BTC","ETH","SOL"])
    volatility = random.randint(2,15)
    situation = "Volatilité normale"
    if volatility > 10: situation = "🚨 Explosion de volatilité"
    elif volatility < 5: situation = "🟢 Marché calme"
    return f"""
⚡ RADAR VOLATILITÉ
{asset} : {safe_price(asset):.0f}$
Volatilité : {volatility}%
Situation : {situation}
"""

# ---------------- RADAR STOP HUNT ----------------
def stop_hunt_radar():
    asset = random.choice(["BTC","ETH","SOL"])
    price = safe_price(asset)
    stop_long = price * 0.97
    stop_short = price * 1.03
    risk = random.randint(20,90)
    situation = "Zone neutre"
    if risk > 70: situation = "🔴 Stop hunt probable"
    elif risk < 40: situation = "🟢 Faible risque"
    return f"""
🎯 RADAR STOP HUNT
Actif : {asset}
Prix : {price:.0f}$
Zone stops longs : {stop_long:.0f}$
Zone stops shorts : {stop_short:.0f}$
Score risque : {risk}/100
Analyse : {situation}
"""

# ---------------- SCANNER COMPLET ----------------
def full_market_scan():
    btc = safe_price("BTC")
    eth = safe_price("ETH")
    sol = safe_price("SOL")
    gold = metal_price("XAU") or 0
    silver = metal_price("XAG") or 0
    sentiment = random.randint(0,100)
    buy = random.randint(30,85)
    sell = random.randint(20,80)
    volatility = random.randint(3,10)
    dominant = random.choice(["BTC","ETH","SOL"])
    direction = "Neutre"
    if sentiment > 65: direction = "🟢 Marché haussier"
    elif sentiment < 40: direction = "🔴 Marché baissier"

    return f"""
🧭 SCANNER COMPLET DU MARCHÉ
CRYPTO : BTC {btc:.0f}$ | ETH {eth:.0f}$ | SOL {sol:.0f}$
METAUX : Gold {gold:.0f}$ | Silver {silver:.0f}$
SENTIMENT : {sentiment}/100
PRESSION MARCHÉ : Acheteurs {buy}% | Vendeurs {sell}%
VOLATILITÉ : {volatility}%
ACTIF DOMINANT : {dominant}
DIRECTION : {direction}
Guide : Comparer sentiment, liquidité et momentum avant toute position.
"""
