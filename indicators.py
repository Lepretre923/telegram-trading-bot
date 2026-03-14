import random

# ---------------- RSI ----------------
def calculate_rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    gains, losses = [], []
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        gains.append(max(diff, 0))
        losses.append(max(-diff, 0))
    avg_gain = sum(gains[-period:])/period
    avg_loss = sum(losses[-period:])/period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

# ---------------- MOVING AVERAGES ----------------
def moving_average(prices, period):
    if len(prices) < period:
        return None
    return round(sum(prices[-period:]) / period, 2)

def ema(prices, period=14):
    if len(prices) < period:
        return None
    k = 2 / (period + 1)
    ema_values = [sum(prices[:period])/period]
    for price in prices[period:]:
        ema_values.append(price * k + ema_values[-1] * (1 - k))
    return round(ema_values[-1], 2)

# ---------------- MACD ----------------
def macd(prices, short_period=12, long_period=26, signal_period=9):
    if len(prices) < long_period:
        return None, None
    short_ema = ema(prices, short_period)
    long_ema_val = ema(prices, long_period)
    macd_line = short_ema - long_ema_val
    signal_line = ema([macd_line]*signal_period, signal_period)  # approximation
    return round(macd_line,2), round(signal_line,2)

# ---------------- BOLLINGER BANDS ----------------
def bollinger_bands(prices, period=20, std_dev_factor=2):
    if len(prices) < period:
        return None, None, None
    sma = moving_average(prices[-period:], period)
    mean = sma
    variance = sum((p - mean)**2 for p in prices[-period:])/period
    std_dev = variance**0.5
    upper = mean + std_dev_factor*std_dev
    lower = mean - std_dev_factor*std_dev
    return round(upper,2), round(mean,2), round(lower,2)

# ---------------- STOCHASTIC OSCILLATOR ----------------
def stochastic_oscillator(prices, period=14):
    if len(prices) < period:
        return None
    high = max(prices[-period:])
    low = min(prices[-period:])
    if high - low == 0:
        return 50
    k = ((prices[-1] - low)/(high - low)) * 100
    return round(k,2)

# ---------------- TREND ANALYSIS ----------------
def simple_trend(prices):
    if len(prices) < 2:
        return "Neutral"
    if prices[-1] > prices[-2]:
        return "Bullish"
    elif prices[-1] < prices[-2]:
        return "Bearish"
    else:
        return "Neutral"

# ---------------- GENERATE INDICATOR REPORT ----------------
def indicator_report(prices):
    rsi_val = calculate_rsi(prices)
    sma_val = moving_average(prices, period=20)
    ema_val = ema(prices, period=20)
    macd_line, macd_signal = macd(prices)
    upper, middle, lower = bollinger_bands(prices)
    stoch = stochastic_oscillator(prices)
    trend = simple_trend(prices)

    return f"""
📊 INDICATORS REPORT

RSI: {rsi_val}
SMA(20): {sma_val}
EMA(20): {ema_val}
MACD: {macd_line} | Signal: {macd_signal}
Bollinger Bands: Upper {upper} | Middle {middle} | Lower {lower}
Stochastic %K: {stoch}
Trend: {trend}
"""
