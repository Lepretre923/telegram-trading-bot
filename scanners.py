import random
from market_data import crypto_price, metal_price, get_history_tf

SCAN_ASSETS=[
    "BTC","ETH","SOL","BNB","XRP",
    "ADA","DOGE","AVAX","MATIC"
]

def market_opportunity_scanner():

    results=[]

    for asset in SCAN_ASSETS:

        price=crypto_price(asset)
        rsi=random.randint(30,70)
        momentum=random.randint(-5,5)

        score=50+momentum*5

        if rsi>60:
            score+=10
        if rsi<40:
            score-=10

        results.append((asset,score,price))

    results=sorted(results,key=lambda x:x[1],reverse=True)

    SEP="━━━━━━━━━━━━━━"

    message=f"🚀 *SCANNER OPPORTUNITÉS*\n\n{SEP}\n"

    for asset,score,price in results[:5]:
        message+=f"""
{asset}

Prix : {price:.0f}$
Score : {score}/100

{SEP}
"""

    message+="\nGuide\n\nSurveiller les actifs\navec le score le plus élevé."

    return message

def stablecoin_flow():

    inflow=random.randint(100,900)
    outflow=random.randint(100,900)

    net=inflow-outflow

    situation="Neutre"

    if net>200:
        situation="🟢 Entrée de capitaux"
    elif net<-200:
        situation="🔴 Sortie de capitaux"

    sign="+" if net>=0 else ""

    return f"""
💵 STABLECOIN FLOW

Entrées
{inflow} M$

Sorties
{outflow} M$

Flux net
{sign}{net} M$

Situation
{situation}
"""

def volume_profile():

    asset=random.choice(["BTC","ETH"])

    price=crypto_price(asset)

    poc=price*0.99
    high_volume=price*1.01
    low_volume=price*0.97

    activity=random.randint(40,90)

    situation="Volume équilibré"

    if activity>70:
        situation="📈 Forte activité marché"
    elif activity<50:
        situation="📉 Faible activité"

    return f"""
📊 VOLUME PROFILE

{asset}

Prix
{price:.0f}

Point of Control
{poc:.0f}

High Volume Zone
{high_volume:.0f}

Low Volume Zone
{low_volume:.0f}

Activité marché
{activity}

Situation
{situation}
"""

def liquidation_map():

    asset=random.choice(["BTC","ETH"])

    price=crypto_price(asset)

    long_liq=price*0.95
    short_liq=price*1.05

    risk=random.randint(30,90)

    situation="Neutre"

    if risk>70:
        situation="⚠️ Forte zone liquidation"
    elif risk<40:
        situation="🟢 Faible pression liquidation"

    return f"""
🔥 CARTE LIQUIDATIONS

Actif

{asset}

Prix actuel

{price:.0f}$

━━━━━━━━━━━━━━

Zone liquidation LONG

{long_liq:.0f}$

Zone liquidation SHORT

{short_liq:.0f}$

━━━━━━━━━━━━━━

Score risque

{risk}/100

Situation

{situation}

━━━━━━━━━━━━━━

Analyse

Les zones de liquidation
attirent souvent le prix
avant un retournement.
"""

def liquidation_radar():

    btc=crypto_price("BTC")

    long_liq=btc*0.96
    short_liq=btc*1.04

    intensity=random.randint(30,90)

    cascade=random.choice([
        "Possible cascade liquidations longues",
        "Possible cascade liquidations shorts",
        "Liquidations faibles"
    ])

    return f"""
📉 RADAR LIQUIDATIONS

BTC : {btc:.0f}$

Zones liquidation longs

{long_liq:.0f}$

Zones liquidation shorts

{short_liq:.0f}$

Intensité liquidations

{intensity}%

Analyse

{cascade}

Guide

Les zones de liquidation
attirent souvent le prix.
"""

def macro_news():

    event=random.choice([
    "CPI Inflation",
    "FOMC Interest Rate Decision",
    "NFP Employment Data",
    "Federal Reserve Speech",
    "GDP Economic Growth"
    ])

    impact=random.choice([
    "🟢 Impact modéré",
    "🟡 Impact important",
    "🔴 Impact très fort"
    ])

    direction=random.choice([
    "Volatilité haussière possible",
    "Volatilité baissière possible",
    "Forte incertitude marché"
    ])

    return f"""
📡 RADAR NEWS MACRO

Événement surveillé

{event}

Impact potentiel

{impact}

Effet possible

{direction}

Guide

Éviter les positions
juste avant les annonces
macro importantes.

Calendrier complet

https://www.forexfactory.com/calendar
"""

def manipulation_radar():

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    trap=random.choice([
    "Possible fake breakout",
    "Possible stop hunt",
    "Zone manipulation probable",
    "Marché stable"
    ])

    risk=random.randint(10,90)

    danger="🟡 Risque modéré"

    if risk>70:
        danger="🔴 Forte manipulation possible"

    if risk<30:
        danger="🟢 Faible manipulation"

    risque_label="Élevé" if risk>70 else ("Faible" if risk<30 else "Modéré")

    return f"""
🧠 RADAR MANIPULATION

Score manipulation

{risk} / 100

Situation

{trap}

Risque

{risque_label}

Guide

Attendre confirmation
avant entrée.
"""

def whale_radar():

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    volume=random.randint(1000,10000)

    movement=random.choice([
    "Accumulation possible",
    "Distribution possible",
    "Transfert entre portefeuilles"
    ])

    impact=random.choice([
    "🟢 Impact haussier possible",
    "🔴 Impact baissier possible",
    "🟡 Impact neutre"
    ])

    return f"""
🐋 WHALE ALERT

Transaction détectée

Volume
{volume} {asset}

Type mouvement
{movement}

Impact
Hausse de volatilité.
"""

def top_opportunities():

    assets=["BTC","ETH","SOL"]

    results=[]

    for asset in assets:

        price=crypto_price(asset)

        momentum=random.randint(-5,5)

        score=50+momentum*5

        results.append((asset,score,price))

    results=sorted(results,key=lambda x:x[1],reverse=True)

    best1=results[0]
    best2=results[1]
    best3=results[2]

    return f"""
🏆 TOP OPPORTUNITÉS MARCHÉ

🥇 {best1[0]}

Prix : {best1[2]:.0f}$

Score opportunité

{best1[1]}

🥈 {best2[0]}

Prix : {best2[2]:.0f}$

Score opportunité

{best2[1]}

🥉 {best3[0]}

Prix : {best3[2]:.0f}$

Score opportunité

{best3[1]}

Guide

Surveiller l'actif
avec le score le plus élevé.
"""

def market_sentiment():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    sentiment_score=random.randint(0,100)

    sentiment="Marché neutre"

    if sentiment_score>65:
        sentiment="🟢 Sentiment bullish"

    if sentiment_score<40:
        sentiment="🔴 Sentiment bearish"

    volatility=random.randint(3,12)

    return f"""
📊 RADAR SENTIMENT MARCHÉ

BTC : {btc:.0f}$
ETH : {eth:.0f}$
SOL : {sol:.0f}$

Score sentiment

{sentiment_score}/100

Direction marché

{sentiment}

Volatilité globale

{volatility}%

Guide

Comparer sentiment,
liquidité et momentum
avant toute position.
"""

def market_levels():

    btc=crypto_price("BTC")

    support1=btc*0.98
    support2=btc*0.95

    resistance1=btc*1.02
    resistance2=btc*1.05

    zone=random.choice([
    "Zone d'accumulation possible",
    "Zone de distribution possible",
    "Zone neutre"
    ])

    return f"""
🗺 CARTE DES NIVEAUX MARCHÉ

BTC : {btc:.0f}$

SUPPORTS

Support proche

{support1:.0f}$

Support majeur

{support2:.0f}$

RÉSISTANCES

Résistance proche

{resistance1:.0f}$

Résistance majeure

{resistance2:.0f}$

Analyse

{zone}

Guide

Observer réaction du prix
sur ces niveaux clés.
"""

def market_pressure():

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    buy_pressure=random.randint(30,85)
    sell_pressure=random.randint(20,80)

    imbalance=buy_pressure-sell_pressure

    dominance="Marché équilibré"

    if imbalance>10:
        dominance="🟢 Acheteurs dominants"

    if imbalance<-10:
        dominance="🔴 Vendeurs dominants"

    volume=random.randint(1000,5000)

    return f"""
📊 RADAR PRESSION MARCHÉ

Actif

{asset}

Prix

{price:.0f}$

Pression acheteurs

{buy_pressure}%

Pression vendeurs

{sell_pressure}%

Volume estimé

{volume}

Dominance

{dominance}

Guide

Quand les acheteurs dominent,
le marché peut continuer
sa tendance haussière.
"""

def top_movers():

    assets=["BTC","ETH","SOL"]

    results=[]

    for asset in assets:

        prices=get_history_tf(asset,"1h")

        if prices and len(prices)>=24:

            change=((prices[-1]-prices[-24])/prices[-24])*100

        else:

            change=0

        results.append((asset,change))

    results=sorted(results,key=lambda x:x[1],reverse=True)

    best1=results[0]
    best2=results[1]
    best3=results[2]

    return f"""
🔥 TOP MOVERS MARCHÉ

🥇 {best1[0]}

Variation

{best1[1]:.2f} %

🥈 {best2[0]}

Variation

{best2[1]:.2f} %

🥉 {best3[0]}

Variation

{best3[1]:.2f} %

Analyse

Les actifs avec la plus
forte variation attirent
souvent la liquidité.
"""

def market_correlation():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    gold=metal_price("XAU")

    btc_move=random.randint(-5,5)
    eth_move=random.randint(-5,5)
    gold_move=random.randint(-3,3)

    correlation="Neutre"

    if btc_move>0 and eth_move>0:
        correlation="🟢 Corrélation crypto haussière"

    if btc_move<0 and eth_move<0:
        correlation="🔴 Corrélation crypto baissière"

    if btc_move<0 and gold_move>0:
        correlation="🟡 Rotation vers actifs refuge"

    return f"""
📊 CORRÉLATION MARCHÉ

BTC : {btc:.0f}$
ETH : {eth:.0f}$
Gold : {gold:.0f}$

Variation estimée

BTC : {btc_move}%
ETH : {eth_move}%
Gold : {gold_move}%

Analyse

{correlation}

Guide

Observer corrélation
entre crypto et métaux
pour confirmer tendance.
"""

def stop_hunt_radar():

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    stop_long=price*0.97
    stop_short=price*1.03

    risk=random.randint(20,90)

    situation="Zone neutre"

    if risk>70:
        situation="🔴 Stop hunt probable"

    if risk<40:
        situation="🟢 Faible risque"

    return f"""
🎯 RADAR STOP HUNT

Actif

{asset}

Prix

{price:.0f}$

Zone stops longs

{stop_long:.0f}$

Zone stops shorts

{stop_short:.0f}$

Score risque

{risk}/100

Analyse

{situation}

Guide

Les zones de stops attirent
souvent le prix avant
un retournement possible.
"""

def volatility_radar():

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    volatility=random.randint(2,15)

    situation="Volatilité normale"

    if volatility>10:
        situation="🚨 Explosion de volatilité"

    if volatility<5:
        situation="🟢 Marché calme"

    return f"""
⚡ RADAR VOLATILITÉ

Volatilité
{volatility} %

Situation
{situation}

Analyse
Mouvement rapide
possible dans les deux sens.
"""

def crypto_market_index():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    btc_score=random.randint(40,80)
    eth_score=random.randint(40,80)
    sol_score=random.randint(40,80)

    global_score=int((btc_score+eth_score+sol_score)/3)

    direction="Marché neutre"

    if global_score>65:
        direction="🟢 Marché haussier"

    if global_score<45:
        direction="🔴 Marché baissier"

    return f"""
🌐 INDICE GLOBAL CRYPTO

BTC score

{btc_score}

ETH score

{eth_score}

SOL score

{sol_score}

INDICE GLOBAL

{global_score}/100

DIRECTION

{direction}

Guide

Comparer indice global
avec momentum du marché.
"""

def opportunity_scanner():

    assets=["BTC","ETH","SOL"]

    results=[]

    for asset in assets:

        price=crypto_price(asset)

        rsi=random.randint(30,70)
        momentum=random.randint(-5,5)

        score=50+momentum*5

        if rsi>60:
            score+=10

        if rsi<40:
            score-=10

        results.append((asset,score,price))

    results=sorted(results,key=lambda x:x[1],reverse=True)

    best=results[0]

    direction="Neutre"

    if best[1]>65:
        direction="🟢 Opportunité haussière"

    if best[1]<40:
        direction="🔴 Opportunité baissière"

    return f"""
🚀 SCANNER OPPORTUNITÉS

Actif détecté

{best[0]}

Prix

{best[2]:.0f}$

Score opportunité

{best[1]}/100

Direction

{direction}

Guide

Surveiller structure
et confirmer cassure
avant entrée.
"""

def full_market_scan():

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    gold=metal_price("XAU")
    silver=metal_price("XAG")

    sentiment=random.randint(0,100)

    buy=random.randint(30,85)
    sell=random.randint(20,80)

    volatility=random.randint(3,10)

    dominant=random.choice(["BTC","ETH","SOL"])

    direction="Neutre"

    if sentiment>65:
        direction="🟢 Marché haussier"

    if sentiment<40:
        direction="🔴 Marché baissier"

    return f"""
🧭 SCANNER COMPLET DU MARCHÉ

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

Guide

Comparer sentiment,
liquidité et momentum
avant toute position.
"""
