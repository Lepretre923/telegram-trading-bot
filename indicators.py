def calculate_rsi(prices,period=14):

    gains=[]
    losses=[]

    for i in range(1,len(prices)):

        diff=prices[i]-prices[i-1]

        if diff>0:
            gains.append(diff)
            losses.append(0)

        else:
            gains.append(0)
            losses.append(abs(diff))

    avg_gain=sum(gains[-period:])/period
    avg_loss=sum(losses[-period:])/period

    if avg_loss==0:
        return 100

    rs=avg_gain/avg_loss

    rsi=100-(100/(1+rs))

    return round(rsi,2)

def moving_average(prices,period):

    if len(prices)<period:
        return None

    return sum(prices[-period:])/period
