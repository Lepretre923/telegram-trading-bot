import random

def btc_crash():
    r = random.randint(1,15)
    if r>12:
        drop = random.randint(6,15)
        return f"🚨 BTC CRASH ALERT\nDrop : -{drop}%\nHigh volatility detected"
    return "BTC stable"

def whale_alert():
    r = random.randint(1,10)
    if r>7:
        btc = random.randint(500,3000)
        return f"🐋 WHALE ALERT\n{btc} BTC moved\nPossible market impact"
    return "No whale detected"
