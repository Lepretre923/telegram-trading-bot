import requests

def crypto_price(asset):
    try:
        r = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={asset.lower()}&vs_currencies=usd").json()
        return r[asset.lower()]["usd"]
    except:
        return 0

def metal_price(asset):
    try:
        # Exemple pour XAU / XAG
        return 1800 if asset=="XAU" else 25
    except:
        return 0

def get_history_tf(asset, timeframe="1h"):
    # Simulation historique prix
    import random
    return [crypto_price(asset) + random.randint(-50,50) for _ in range(24)]
