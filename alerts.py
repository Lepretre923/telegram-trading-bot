import random

def crash():
    r = random.randint(1, 15)
    if r > 12:
        drop = random.randint(6, 15)
        return f"🚨 BTC CRASH ALERT\nDrop: -{drop}%"
    return "BTC stable"

def whale_alert():
    r = random.randint(1, 10)
    if r > 7:
        btc = random.randint(500, 3000)
        return f"🐋 WHALE ALERT\n{btc} BTC moved"
    return "No whale detected"
