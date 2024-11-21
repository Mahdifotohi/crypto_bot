import requests
import json
import time

url = 'https://api.nobitex.ir/v3/orderbook/all'

crypto_dict = {
   'btc': 'BTCIRT', 'eth': 'ETHIRT', 'ton': 'TONIRT', 'trx': 'TRXIRT',
   'dogs': 'DOGSIRT', 'hamester': 'HMSTRIRT', 'cati': 'CATIIRT', 'not': 'NOTIRT',
   'usdt': 'USDTIRT',
   }

# receive respons request api
def respons(crypto_name):
    while True:
      respons = requests.get(url)
      data = respons.json()
      time.sleep(1)
      return data[crypto_name]



#  receive respons for api coin price to IRT
def last_price(crypto_name):
   for name in crypto_dict.keys():
      if name == crypto_name:
         data = respons(crypto_dict[name])
   last_price = data['lastTradePrice']
   return last_price


# convert to format standard
def format_price(price, crypto_name):
   format_price = crypto_name + ": " + f"{round(price / 10):,.0f} Toman"
   return format_price

#extract number and letter to input crypto_name
def extract_numbers(crypto_name):
   numbers = ''
   letters = ''
   for char in crypto_name:
      if char.isdigit():
         numbers += char
      else:
         letters += char
         if numbers == '':
            numbers = '1'
   return numbers, letters

#receive to value price ex:100 not
def value_price(crypto_name='1 btc'):
   number, letter = extract_numbers(crypto_name)
   last_price2 = last_price(letter.lower().strip())
   price = int(number) * int(last_price2)
   return format_price(price, crypto_name)



