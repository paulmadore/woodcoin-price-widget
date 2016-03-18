#!/usr/bin/python3
# coding=utf-8
import requests
from urllib.request import urlopen
import cgi

def prices():
    logbtc = requests.get('https://c-cex.com/t/log-btc.json')
    logbtc_text = logbtc.text
    logbtc_json = json.loads(logbtc_text)
    log = logbtc_json['ticker']['lastprice']
    btcusd = requests.get('https://api.bitcoinaverage.com/ticker/global/all')
    btcusd_text = btcusd.text
    btcusd_json = json.loads(btcusd_text)
    btcout = btcusd_json['USD']['last']
    usd = log * btcout

print('Content-type: text/html')
print('<html><head><link rel="stylesheet" href="price.css"></head><body>')
print('<div id="pricebox"><div id="box1">' + log + ' BTC/LOG</div><div id="box2">' + usd + 'USD/LOG</div>')
print('</body></html>')
    
