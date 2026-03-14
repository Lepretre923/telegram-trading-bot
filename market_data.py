import requests

def crypto_price(symbol: str):
    try:
        r = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd"
        ).json()
        return r[symbol.lower()]["usd"]
    except Exception:
        return 0

def metal_price(symbol: str):
    try:
        prices = {"XAU": 2000, "XAG": 25}
        return prices.get(symbol.upper(), 0)
    except Exception:
        return 0

def get_history_tf(symbol: str, timeframe: str):
    try:
        import random
        return [crypto_price(symbol) + random.uniform(-5, 5) for _ in range(24)]
    except Exception:
        return []
