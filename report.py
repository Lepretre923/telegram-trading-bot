from analysis import market_analysis, btc_chart
from signals import trading_signal
from intel import crypto_news

def full_report():
    return f"""
📋 GLOBAL MARKET REPORT

{market_analysis()}

{trading_signal()}

{crypto_news()}

{btc_chart()}
"""
