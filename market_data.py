import requests

def crypto_price(symbol):
    try:
        r = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd").json()
        return r[symbol.lower()]["usd"]
    except:
        return 0

def metal_price(symbol):
    # Ex: XAU = Gold, XAG = Silver
    prices = {"XAU": 2000, "XAG": 25}  # Valeurs fictives si pas d'API
    return prices.get(symbol.upper(), 0)

def get_history_tf(symbol, tf="1h"):
    # Fonction simplifiée pour retourner des prix fictifs pour scanner
    import random
    return [random.randint(1000, 30000) for _ in range(50)]
