import requests

def crypto_price(asset):
    try:
        r = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={asset.lower()}&vs_currencies=usd").json()
        return r[asset.lower()]["usd"]
    except:
        return 0

def metal_price(symbol):
    # Simulation, remplacer par API réelle si nécessaire
    mapping = {"XAU": 1950, "XAG": 25}
    return mapping.get(symbol, 0)
