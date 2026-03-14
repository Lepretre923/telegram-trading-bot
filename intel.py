import requests

def crypto_news():
    try:
        r = requests.get("https://cryptopanic.com/api/v1/posts/?public=true").json()
        return "📰 " + r["results"][0]["title"]
    except:
        return "News unavailable"
