import requests

# ---------------- PRIX BTC ----------------

def btc_price():

    try:

        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": "bitcoin",
                "vs_currencies": "usd"
            },
            timeout=5
        )

        data = r.json()

        return data["bitcoin"]["usd"]

    except Exception:

        return None


# ---------------- PRIX ETH ----------------

def eth_price():

    try:

        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": "ethereum",
                "vs_currencies": "usd"
            },
            timeout=5
        )

        data = r.json()

        return data["ethereum"]["usd"]

    except Exception:

        return None


# ---------------- TOP GAINERS ----------------

def top_gainers():

    try:

        r = requests.get(
            "https://api.coingecko.com/api/v3/coins/markets",
            params={
                "vs_currency": "usd",
                "order": "percent_change_24h_desc",
                "per_page": 5,
                "page": 1
            },
            timeout=5
        )

        data = r.json()

        msg = "🚀 TOP GAINERS 24H\n\n"

        for coin in data:

            name = coin["name"]
            symbol = coin["symbol"].upper()
            change = round(coin["price_change_percentage_24h"], 2)

            msg += f"{name} ({symbol})  +{change}%\n"

        msg += "\nAnalyse\nLes actifs avec forte variation attirent souvent la liquidité."

        return msg

    except Exception:

        return "Impossible de récupérer les top gainers."
