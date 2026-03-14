import random
from market_data import crypto_price, metal_price

def crash():
    risk=random.randint(3,12)
    return f"🚨 Crash possible : -{risk}%"

def whale():

    volume=random.randint(2000,9000)

    return f"""
🐋 WHALE ALERT

Transaction estimée

{volume} BTC
"""

async def opportunity_alert(context):

    assets=["BTC","ETH","SOL"]

    for asset in assets:

        price=crypto_price(asset)

        rsi=random.randint(30,70)
        momentum=random.randint(-5,5)

        if rsi>65 and momentum>3:

            msg=f"""
🚀 OPPORTUNITÉ MARCHÉ

Actif

{asset}

Prix

{price:.0f}$

RSI

{rsi}

Momentum

{momentum}

Analyse

Possible impulsion haussière.

Guide

Surveiller cassure
de résistance proche.
"""

            await context.bot.send_message(
                chat_id=context.job.chat_id,
                text=msg,
                parse_mode="Markdown"
            )

async def breakout_alert(context):

    assets=["BTC","ETH","SOL"]

    for asset in assets:

        price=crypto_price(asset)

        resistance=price*1.02
        support=price*0.98

        move=random.randint(-5,5)

        if move>3:

            msg=f"""
📈 BREAKOUT HAUSSIER

Actif

{asset}

Prix actuel

{price:.0f}$

Résistance cassée

{resistance:.0f}$

Analyse

Possible impulsion haussière.

Guide

Surveiller continuation
de la tendance.
"""

            await context.bot.send_message(
                chat_id=context.job.chat_id,
                text=msg,
                parse_mode="Markdown"
            )

        if move<-3:

            msg=f"""
📉 BREAKOUT BAISSIER

Actif

{asset}

Prix actuel

{price:.0f}$

Support cassé

{support:.0f}$

Analyse

Possible impulsion baissière.

Guide

Attention aux liquidations
longues.
"""

            await context.bot.send_message(
                chat_id=context.job.chat_id,
                text=msg,
                parse_mode="Markdown"
            )

last_prices={}

async def market_alert(context):

    global last_prices

    assets=["BTC","ETH","SOL"]

    for asset in assets:

        price=crypto_price(asset)

        if price is None:
            continue

        if asset not in last_prices:
            last_prices[asset]=price
            continue

        change=((price-last_prices[asset])/last_prices[asset])*100

        if abs(change)>=3:

            message=f"""
🚨 ALERTE MOUVEMENT

{asset}

Prix : {price:.0f}$

Variation

{change:.2f} %

Mouvement important détecté.
"""

            await context.bot.send_message(
                chat_id=context.job.chat_id,
                text=message,
                parse_mode="Markdown"
            )

            last_prices[asset]=price

async def auto_market_report(context):

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    gold=metal_price("XAU")
    silver=metal_price("XAG")

    sentiment=random.randint(0,100)

    direction="Neutre"

    if sentiment>65:
        direction="🟢 Marché haussier"

    if sentiment<40:
        direction="🔴 Marché baissier"

    message=f"""
📊 RAPPORT AUTOMATIQUE MARCHÉ

CRYPTO

BTC : {btc:.0f}$
ETH : {eth:.0f}$
SOL : {sol:.0f}$

METAUX

Gold : {gold:.0f}$
Silver : {silver:.0f}$

Sentiment global

{sentiment}/100

Direction

{direction}

Analyse

Comparer liquidité,
momentum et sentiment
avant toute décision.
"""

    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=message,
        parse_mode="Markdown"
    )

async def daily_report(context):

    btc=crypto_price("BTC")
    eth=crypto_price("ETH")
    sol=crypto_price("SOL")

    gold=metal_price("XAU")
    silver=metal_price("XAG")

    sentiment=random.randint(0,100)

    direction="Neutre"

    if sentiment>65:
        direction="🟢 Marché haussier"

    if sentiment<40:
        direction="🔴 Marché baissier"

    message=f"""
📊 RAPPORT MARCHÉ AUTOMATIQUE

CRYPTO

BTC : {btc:.0f}$
ETH : {eth:.0f}$
SOL : {sol:.0f}$

METAUX

Gold : {gold:.0f}$
Silver : {silver:.0f}$

Sentiment marché

{sentiment}/100

Direction

{direction}

Guide

Comparer tendance
et liquidité avant trade.
"""

    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=message,
        parse_mode="Markdown"
    )

async def daily_trade_plan(context):

    asset=random.choice(["BTC","ETH","SOL"])

    price=crypto_price(asset)

    entry_low=price*0.995
    entry_high=price*1.005

    stop=price*0.97
    target=price*1.04

    direction=random.choice([
    "🟢 Opportunité haussière",
    "🔴 Opportunité baissière",
    "🟡 Attendre confirmation"
    ])

    probability=random.randint(50,80)

    message=f"""
📈 *PLAN DE TRADE*

*Actif*
{asset}

*Prix actuel*
{price:.0f} $

*Zone d'entrée*
{entry_low:.0f} - {entry_high:.0f} $

*Stop loss*
{stop:.0f} $

*Objectif*
{target:.0f} $

*Probabilité*
{probability} %

*Guide*
Entrer seulement si
la tendance confirme.
"""

    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=message,
        parse_mode="Markdown"
    )

async def danger_alert(context):

    assets=["BTC","ETH","SOL"]

    for asset in assets:

        price=crypto_price(asset)

        drop=random.randint(-10,5)

        if drop<-6:

            support1=price*0.975
            support2=price*0.95

            message=f"""
🚨 CRASH ALERT

Risque de correction

{drop} %

Facteurs détectés

RSI en surchauffe
Volatilité élevée
Pression vendeuse

Zones sensibles

Support critique
{support1:.0f} $

Support majeur
{support2:.0f} $

Analyse

Une correction rapide
reste possible si
le support casse.
"""

            await context.bot.send_message(
                chat_id=context.job.chat_id,
                text=message,
                parse_mode="Markdown"
            )
