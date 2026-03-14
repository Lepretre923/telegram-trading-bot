# reports.py
from analysis import market_analysis, btc_chart
from signals import trading_signal
from intel import crypto_news

def full_report():
    """
    Génère un rapport complet incluant :
    - Analyse du marché (RSI, MACD, Sentiment)
    - Graphique BTC
    - Signal trading
    - Dernières news crypto
    """
    report = f"""
📋 GLOBAL MARKET REPORT

--- Market Analysis ---
{market_analysis()}

--- BTC Chart ---
{btc_chart()}

--- Trading Signal ---
{trading_signal()}

--- Latest Crypto News ---
{crypto_news()}

Guide:
- Comparer les analyses et signaux avant toute action.
- Vérifier les zones de support/résistance et liquidité avant trade.
"""
    return report
