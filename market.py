import requests

def btc_price():
    try:
        r=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        return r["bitcoin"]["usd"]
    except:
        return "N/A"

def eth_price():
    try:
        r=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd").json()
        return r["ethereum"]["usd"]
    except:
        return "N/A"

def top_gainers():

    try:

        r=requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=percent_change_24h_desc&per_page=5&page=1").json()

        msg="🚀 TOP GAINERS\n\n"

        for coin in r:

            name=coin["name"]
            change=round(coin["price_change_percentage_24h"],2)

            msg+=f"{name} +{change}%\n"

        return msg

    except:

        return "Unavailable"
