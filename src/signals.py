import random

def get_signal():

    coins=["BTC","ETH","SOL","AVAX","LINK"]

    coin=random.choice(coins)

    confidence=random.randint(60,95)

    return f"""
📈 Signal trading détecté

Crypto : {coin}

Confiance : {confidence}%
"""