import random

def btc_crash():

    r=random.randint(1,15)

    if r>12:

        drop=random.randint(6,15)

        return f"""
🚨 BTC CRASH ALERT

Drop : -{drop}%
High volatility detected
"""

    return "BTC stable"
