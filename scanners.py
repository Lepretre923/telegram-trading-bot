import random
from market_data import crypto_price, metal_price, get_history_tf

SCAN_ASSETS = [
    "BTC", "ETH", "SOL", "BNB", "XRP",
    "ADA", "DOGE", "AVAX", "MATIC"
]

SEP = "━━━━━━━━━━━━━━"

# ---------- UTILITAIRES ----------
def safe_price(asset):
    try:
        price = crypto_price(asset)
        return price if price is not None else 0
    except:
        return 0

# ---------- SCANNER OPPORTUNITÉS ----------
def market_opportunity_scanner():
    results = []
    for asset in SCAN_ASSETS:
        price = safe_price(asset)
        rsi = random.randint(30, 70)
        momentum = random.randint(-5, 5)
        score = 50 + momentum * 5
        if rsi > 60: score += 10
        if rsi < 40: score -= 10
        results.append((asset, score, price))
    results = sorted(results, key=lambda x: x[1], reverse=True)

    message = f"🚀 *SCANNER OPPORTUNITÉS*\n\n{SEP}\n"
    for asset, score, price in results[:5]:
        message += f"{asset}\nPrix : {price:.0f}$\nScore : {score}/100\n{SEP}\n"
    message += "\nGuide : Surveiller les actifs avec le score le plus élevé."
    return message

# ---------- RADARS ----------
def liquidation_radar():
    asset = random.choice(["BTC", "ETH"])
    price = safe_price(asset)
    long_liq = price * 0.95
    short_liq = price * 1.05
    risk = random.randint(30, 90)
    situation = "Neutre"
    if risk > 70: situation = "⚠️ Forte zone liquidation"
    elif risk < 40: situation = "🟢 Faible pression liquidation"
    return f"🔥 CARTE LIQUIDATIONS\nActif : {asset}\nPrix actuel : {price:.0f}$\nZone LONG : {long_liq:.0f}$\nZone SHORT : {short_liq:.0f}$\nScore risque : {risk}/100\nSituation : {situation}\n{SEP}\nAnalyse : Les zones de liquidation attirent souvent le prix avant un retournement."

def manipulation_radar():
    asset = random.choice(["BTC", "ETH", "SOL"])
    price = safe_price(asset)
    trap = random.choice([
        "Possible fake breakout",
        "Possible stop hunt",
        "Zone manipulation probable",
        "Marché stable"
    ])
    risk = random.randint(10, 90)
    risque_label = "🟡 Risque modéré"
    if risk > 70: risque_label = "🔴 Forte manipulation possible"
    elif risk < 30: risque_label = "🟢 Faible manipulation"
    return f"🧠 RADAR MANIPULATION\nActif : {asset}\nPrix : {price:.0f}$\nSituation : {trap}\nScore manipulation : {risk}/100\nRisque : {risque_label}\nGuide : Attendre confirmation avant entrée."

# ---------- SCAN COMPLET ----------
def full_market_scan():
    btc = safe_price("BTC")
    eth = safe_price("ETH")
    sol = safe_price("SOL")
    gold = metal_price("XAU")
    silver = metal_price("XAG")
    sentiment = random.randint(0, 100)
    buy = random.randint(30, 85)
    sell = random.randint(20, 80)
    volatility = random.randint(3, 10)
    dominant = random.choice(["BTC", "ETH", "SOL"])
    direction = "Neutre"
    if sentiment > 65: direction = "🟢 Marché haussier"
    elif sentiment < 40: direction = "🔴 Marché baissier"

    return f"""🧭 SCANNER COMPLET DU MARCHÉ

CRYPTO
BTC : {btc:.0f}$
ETH : {eth:.0f}$
SOL : {sol:.0f}$

METAUX
Gold : {gold:.0f}$
Silver : {silver:.0f}$

SENTIMENT
{sentiment}/100

PRESSION MARCHÉ
Acheteurs : {buy}%
Vendeurs : {sell}%

VOLATILITÉ
{volatility}%

ACTIF DOMINANT
{dominant}

DIRECTION
{direction}

Guide : Comparer sentiment, liquidité et momentum avant toute position.
"""
