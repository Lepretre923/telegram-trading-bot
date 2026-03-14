from market import get_price,top_crypto
from analysis import analyse
from signals import get_signal
from intel import market_intel,market_scanner,sentiment_crypto

def market_report():

    msg="📊 Rapport complet marché\n\n"

    msg+=get_price("BTC")+"\n"
    msg+=get_price("ETH")+"\n\n"

    msg+=analyse("BTC")+"\n"

    msg+=get_signal()+"\n"

    msg+=market_intel()+"\n"

    msg+=market_scanner()+"\n"

    msg+=sentiment_crypto()+"\n"

    msg+=top_crypto()

    return msg