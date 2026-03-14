import random
from market_data import crypto_price


def trading_signal():

    asset = random.choice(["BTC", "ETH", "SOL"])

    price = crypto_price(asset)

    rsi = random.randint(30,70)

    momentum = random.randint(-5,5)

    signal = "HOLD"

    if rsi > 60 and momentum > 1:
        signal = "BUY"

    elif rsi < 40 and momentum < -1:
        signal = "SELL"

    probability = random.randint(55,85)

    entry_low = price * 0.995
    entry_high = price * 1.005

    stop_loss = price * 0.97

    take_profit = price * 1.04

    support = price * 0.98

    resistance = price * 1.02

    direction="Marché neutre"

    if signal=="BUY":
        direction="🟢 Setup haussier"

    elif signal=="SELL":
        direction="🔴 Setup baissier"

    return f"""
📈 TRADING SIGNAL

━━━━━━━━━━━━━━━━━━

Actif
{asset}

Prix actuel
{price:.0f}$

━━━━━━━━━━━━━━━━━━

Action
{signal}

Probabilité
{probability}%

━━━━━━━━━━━━━━━━━━

Zone entrée

{entry_low:.0f}$ - {entry_high:.0f}$

Stop Loss

{stop_loss:.0f}$

Take Profit

{take_profit:.0f}$

━━━━━━━━━━━━━━━━━━

Structure marché

Support
{support:.0f}$

Résistance
{resistance:.0f}$

━━━━━━━━━━━━━━━━━━

Analyse

RSI : {rsi}
Momentum : {momentum:+}

Direction

{direction}

━━━━━━━━━━━━━━━━━━

Guide

Entrer seulement si
le prix confirme
la direction du signal.
"""
