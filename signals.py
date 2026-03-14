import random

def trading_signal():
    signal = random.choice(["BUY", "SELL", "HOLD"])
    probability = random.randint(55, 90)
    return f"📈 TRADING SIGNAL\nAction: {signal}\nProbability: {probability}%"
