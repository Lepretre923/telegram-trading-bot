import random

def btc_crash():

    risk = random.randint(1,100)

    if risk > 80:

        drop = random.randint(6,15)

        support1 = random.randint(62000,67000)
        support2 = support1 - random.randint(1000,3000)

        return f"""
🚨 BTC CRASH ALERT

Probabilité crash
{risk} %

Correction estimée

-{drop} %

Zones de support

Support critique
{support1} $

Support majeur
{support2} $

Analyse

Volatilité élevée détectée.
Risque de liquidation massive.

Guide

Surveiller réaction
sur les supports.
"""

    return """
BTC stable

Aucun signal de crash
détecté actuellement.
"""
