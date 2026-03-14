# indicator.py
import random

def calculate_rsi(prices, period=14):
    """
    Calcul du RSI (Relative Strength Index) pour une liste de prix.
    Retourne un float arrondi à 2 décimales.
    """
    if len(prices) < period + 1:
        return None

    gains, losses = [], []

    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        if diff > 0:
            gains.append(diff)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(diff))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)


def moving_average(prices, period=20):
    """
    Calcul de la moyenne mobile simple sur une liste de prix.
    Retourne None si pas assez de données.
    """
    if len(prices) < period:
        return None
    return round(sum(prices[-period:]) / period, 2)


def exponential_moving_average(prices, period=20):
    """
    Calcul de la moyenne mobile exponentielle (EMA) sur une liste de prix.
    """
    if len(prices) < period:
        return None

    ema = prices[0]
    k = 2 / (period + 1)

    for price in prices[1:]:
        ema = price * k + ema * (1 - k)

    return round(ema, 2)


def bollinger_bands(prices, period=20, std_dev=2):
    """
    Calcul des bandes de Bollinger (SMA ± std_dev * écart-type)
    """
    if len(prices) < period:
        return None, None, None

    sma = moving_average(prices[-period:], period)
    mean = sum(prices[-period:]) / period
    variance = sum((p - mean) ** 2 for p in prices[-period:]) / period
    std = variance ** 0.5

    upper_band = round(sma + std_dev * std, 2)
    lower_band = round(sma - std_dev * std, 2)
    return lower_band, sma, upper_band


def macd(prices, short_period=12, long_period=26, signal_period=9):
    """
    Calcul du MACD et de sa ligne de signal.
    Retourne (macd_value, signal_value)
    """
    if len(prices) < long_period + signal_period:
        return None, None

    ema_short = exponential_moving_average(prices[-short_period:])
    ema_long = exponential_moving_average(prices[-long_period:])
    macd_value = ema_short - ema_long

    signal_line = exponential_moving_average([macd_value]*signal_period, signal_period)
    return round(macd_value, 2), round(signal_line, 2)


def generate_random_indicator_signal():
    """
    Génère un signal aléatoire basé sur des indicateurs pour les tests ou le bot.
    """
    return random.choice(["BUY", "SELL", "HOLD"])
