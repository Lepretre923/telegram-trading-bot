import os
import requests
import time
import threading
import datetime
from flask import Flask

from market import btc_price,eth_price,top_gainers
from analysis import market_analysis,btc_chart
from signals import trading_signal
from alerts import btc_crash
from intel import whale_alert,crypto_news
from report import full_report

app = Flask('')

@app.route('/')
def home():
    return "Bot running"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()

TOKEN=os.environ.get("TELEGRAM_BOT_TOKEN")

URL=f"https://api.telegram.org/bot{TOKEN}/"

offset=None
CHAT_ID=None


def send(chat,text,keyboard=None):

    data={"chat_id":chat,"text":text}

    if keyboard:
        data["reply_markup"]=keyboard

    requests.post(URL+"sendMessage",json=data)



def dashboard(chat):

    keyboard={
    "keyboard":[

    ["💰 BTC","💰 ETH"],

    ["📊 Analyse marché","📈 Graphique BTC"],

    ["📉 Signal trading","🚀 Top gainers"],

    ["🐋 Whale alert","🚨 Crash BTC"],

    ["📰 News crypto"],

    ["📋 Rapport complet"]

    ],
    "resize_keyboard":True
    }

    send(chat,"📊 TRADING DASHBOARD",keyboard)



def auto_reports():

    while True:

        if CHAT_ID:

            hour=datetime.datetime.now().hour

            if hour==8:
                send(CHAT_ID,"☀️ Morning Report\n"+full_report())

            if hour==13:
                send(CHAT_ID,"📊 Midday Report\n"+full_report())

            if hour==20:
                send(CHAT_ID,"🌙 Evening Report\n"+full_report())

        time.sleep(3600)



def report_2h():

    while True:

        if CHAT_ID:
            send(CHAT_ID,"📊 Market Update\n"+market_analysis())

        time.sleep(7200)



threading.Thread(target=auto_reports).start()
threading.Thread(target=report_2h).start()



while True:

    try:

        r=requests.get(URL+"getUpdates",params={"offset":offset}).json()

        for update in r["result"]:

            offset=update["update_id"]+1

            chat=update["message"]["chat"]["id"]

            text=update["message"].get("text","")

            if text=="/start":

                CHAT_ID=chat
                dashboard(chat)



            if text=="💰 BTC":
                send(chat,str(btc_price()))

            if text=="💰 ETH":
                send(chat,str(eth_price()))

            if text=="📊 Analyse marché":
                send(chat,market_analysis())

            if text=="📈 Graphique BTC":
                send(chat,btc_chart())

            if text=="📉 Signal trading":
                send(chat,trading_signal())

            if text=="🚀 Top gainers":
                send(chat,top_gainers())

            if text=="🐋 Whale alert":
                send(chat,whale_alert())

            if text=="🚨 Crash BTC":
                send(chat,btc_crash())

            if text=="📰 News crypto":
                send(chat,crypto_news())

            if text=="📋 Rapport complet":
                send(chat,full_report())

    except:
        pass

    time.sleep(2)
