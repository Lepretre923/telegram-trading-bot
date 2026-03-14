import random
from market_data import crypto_price

def market_opportunity_scanner():
    assets = ["BTC", "ETH", "SOL", "BNB", "XRP"]
    message = "🚀 SCANNER OPPORTUNITÉS\n"
    for asset in assets:
        price = crypto_price(asset)
        score = random.randint(30, 100)
        message += f"{asset}: {price}$ - Score {score}/100\n"
    return message

def liquidation_radar():
    btc = crypto_price("BTC")
    return f"🔥 RADAR LIQUIDATIONS BTC: {btc}$"
