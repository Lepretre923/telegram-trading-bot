# intel.py
import requests

def crypto_news():
    """
    Récupère la dernière actualité crypto depuis l'API publique Cryptopanic.
    """
    try:
        r = requests.get("https://cryptopanic.com/api/v1/posts/?public=true").json()
        # On prend le titre du dernier article
        return "📰 " + r["results"][0]["title"]
    except:
        return "News unavailable"
