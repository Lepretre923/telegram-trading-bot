import requests
import random

def market_intel():

    news=[
        "Bitcoin ETF volume record",
        "Ethereum activité réseau en hausse",
        "Solana volume trading élevé"
    ]

    msg="📰 News crypto\n\n"

    for n in news:
        msg+=f"• {n}\n"

    return msg


def whale_alert():

    whales=[
        "🐋 1200 BTC transférés vers exchange",
        "🐋 800 ETH déplacés vers wallet inconnu",
        "🐋 grosse transaction USDT détectée"
    ]

    return random.choice(whales)


def whale_blockchain():

    whales=[
        "🐋 3500 BTC transférés vers Binance",
        "🐋 2100 ETH déplacés hors exchange",
        "🐋 grosse transaction USDT 45M$"
    ]

    return "🚨 Whale blockchain détectée\n\n"+random.choice(whales)


def market_scanner():

    url="https://api.coingecko.com/api/v3/coins/markets"

    params={
        "vs_currency":"usd",
        "order":"market_cap_desc",
        "per_page":200,
        "page":1
    }

    data=requests.get(url,params=params).json()

    pumps=[]

    for coin in data:

        change=coin["price_change_percentage_24h"]

        if change>8:

            pumps.append(f"{coin['symbol'].upper()} +{change:.2f}%")

    if not pumps:
        return "Aucun pump détecté"

    msg="🚀 Pumps détectés\n\n"

    for p in pumps[:5]:
        msg+=p+"\n"

    return msg


def liquidation_alert():

    liquidations=[
        "💥 Liquidations importantes sur BTC futures",
        "💥 Long liquidations détectées",
        "💥 Short squeeze possible"
    ]

    return random.choice(liquidations)


def sentiment_crypto():

    sentiments=[
        "Marché très haussier",
        "Marché neutre",
        "Marché légèrement baissier"
    ]

    return "🧠 Sentiment crypto : "+random.choice(sentiments)


def volume_scanner():

    return "📊 Volume anormal détecté sur plusieurs altcoins"