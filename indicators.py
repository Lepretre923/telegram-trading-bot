import pandas as pd

# -------------------- RSI --------------------
def calculate_rsi(prices, period=14):
    """
    Calcul du RSI (Relative Strength Index)
    :param prices: liste ou pandas Series des prix
    :param period: période de calcul (défaut 14)
    :return: RSI arrondi à 2 décimales
    """
    if len(prices) < period + 1:
        return None

    deltas = pd.Series(prices).diff()
    gains = deltas.clip(lower=0)
    losses = -deltas.clip(upper=0)

    avg_gain = gains.rolling(period).mean().iloc[-1]
    avg_loss = losses.rolling(period).mean().iloc[-1]

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)


# -------------------- SMA / EMA --------------------
def simple_moving_average(prices, period=20):
    """
    Moyenne mobile simple
    """
    if len(prices) < period:
        return None
    return round(pd.Series(prices).rolling(period).mean().iloc[-1], 2)

def exponential_moving_average(prices, period=20):
    """
    Moyenne mobile exponentielle
    """
    if len(prices) < period:
        return None
    return round(pd.Series(prices).ewm(span=period, adjust=False).mean().iloc[-1], 2)


# -------------------- MACD --------------------
def calculate_macd(prices, fast=12, slow=26, signal=9):
    """
    MACD = EMA(fast) - EMA(slow)
    """
    if len(prices) < slow + signal:
        return None, None

    df = pd.Series(prices)
    ema_fast = df.ewm(span=fast, adjust=False).mean()
    ema_slow = df.ewm(span=slow, adjust=False).mean()

    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()

    return round(macd_line.iloc[-1], 2), round(signal_line.iloc[-1], 2)


# -------------------- Bollinger Bands --------------------
def bollinger_bands(prices, period=20, std_dev=2):
    """
    Bandes de Bollinger
    :return: (middle, upper, lower)
    """
    if len(prices) < period:
        return None, None, None

    df = pd.Series(prices)
    sma = df.rolling(period).mean().iloc[-1]
    std = df.rolling(period).std().iloc[-1]

    upper = sma + std_dev * std
    lower = sma - std_dev * std
    return round(sma, 2), round(upper, 2), round(lower, 2)
