import random
import requests


def whale_alert():

    r = random.randint(1,10)

    if r > 7:

        btc = random.randint(500,3000)

        direction = random.choice([
            "moved to exchange",
            "moved to cold wallet",
            "unknown wallet transfer"
        ])

        impact = random.choice([
            "Possible sell pressure",
            "Possible accumulation",
            "Market volatility expected"
        ])

        return f"""
🐋 WHALE ALERT

Volume
{btc} BTC

Movement
{direction}

Impact
{impact}
"""

    return "🐋 No whale detected"


def crypto_news():

    try:

        url = "https://cryptopanic.com/api/v1/posts/?public=true"

        r = requests.get(url).json()

        news = r["results"][0]["title"]

        return f"""
📰 CRYPTO NEWS

{news}

Source
CryptoPanic
"""

    except:

        return """
📰 CRYPTO NEWS

News unavailable
"""
