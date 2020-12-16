import tweepy
import sys
import requests
import json
import time


API_KEY = "API Keys goe here"
SECRET_KEY =  "Secret key goes here"
ACCESS_TOKEN = "ACCES TOKEN GOES HERE"
ACCESS_TOKEN_SECRET = "ACCESS TOKEN SECRET GOES HERE"

auth_handler = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=SECRET_KEY)
auth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

#me = api.me()   Personal Info
print('logged in succesfully')

while True:
    etherprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
    bitcoinprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    xrpprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
    price = etherprice.json()
    bitcoin = bitcoinprice.json()
    xrp = xrpprice.json()
    priceusd = price['ethereum']['usd']
    btcusd = bitcoin['bitcoin']['usd']
    xrpusd = xrp['ripple']['usd']

    message = 'current #Ethereum Price: ' + str(priceusd) + ' USD\nTrade #Ethereum  \nnow at 🚀https://bit.ly/3mpFwii - Bybit 🚀 \n #crypto #eth #earncrypto #tothemoon'
    message2 = 'current #BTC Price ' + str(btcusd) + ' USD \n Go long on #BTC now on BYBIT 🚀https://bit.ly/3mpFwii🚀🚀'

    api.update_status(message)
    print(priceusd)
    print('tweet was posted')
    time.sleep(2)
    api.update_status(message2)
    print('tweet was sent')
    time.sleep(2)
    if btcusd > int(20800):
        alltime = f'Bitcoin just reached ALL TIME HIGH 🚀🚀🚀 Price: {btcusd} \nBuy #bitcoin on #Bitpanda https://bit.ly/3agRA2V '
        api.update_status(alltime)
    time.sleep(300)
