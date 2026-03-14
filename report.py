from analysis import market_analysis
from signals import trading_signal
from intel import crypto_news

def full_report():
    return f"📋 GLOBAL MARKET REPORT\n\n{market_analysis()}\n{trading_signal()}\n{crypto_news()}"
