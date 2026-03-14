import requests

def crypto_price(asset):
    try:
        r = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={asset.lower()}&vs_currencies=usd").json()
        return r[asset.lower()]["usd"]
    except:
        return 0

def metal_price(asset):
    prices = {"XAU": 2000, "XAG": 25}
    return prices.get(asset, 0)
