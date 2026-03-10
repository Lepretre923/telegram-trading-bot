import random
import requests

def whale_alert():

    r=random.randint(1,10)

    if r>7:

        btc=random.randint(500,3000)

        return f"""
🐋 WHALE ALERT

{btc} BTC moved
Possible market impact
"""

    return "No whale detected"


def crypto_news():

    try:

        r=requests.get("https://cryptopanic.com/api/v1/posts/?public=true").json()

        return "📰 "+r["results"][0]["title"]

    except:

        return "News unavailable"
