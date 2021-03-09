import requests
from bs4 import BeautifulSoup
import html2text

#Bitcoin Stats
url_btc = "https://coinmarketcap.com/currencies/bitcoin/markets/"
req = requests.get(url_btc)
soup = BeautifulSoup(req.content, 'html.parser')
price_btc = soup.find("div", {"class": "priceValue___11gHJ"})
precent_btc = soup.find("span",{"class": "qe1dn9-0 RYkpI"})

print("Bitcoin: ")
print(price_btc.text)
print(precent_btc.text + " up/down" + "\n")


#Ethereum Stats
url_eth = "https://coinmarketcap.com/currencies/ethereum/"
req = requests.get(url_eth)
soup = BeautifulSoup(req.content, 'html.parser')
price_eth = soup.find("div", {"class": "priceValue___11gHJ"})
precent_eth = soup.find("span",{"class": "qe1dn9-0 RYkpI"})

print("Ethereum: ")
print(price_eth.text)
print(precent_eth.text + " up/down" + "\n")


#Binance Coin Stats
url_bnb = "https://coinmarketcap.com/currencies/binance-coin/"
req = requests.get(url_bnb)
soup = BeautifulSoup(req.content, 'html.parser')
price_bnb = soup.find("div", {"class": "priceValue___11gHJ"})
precent_bnb = soup.find("span",{"class": "qe1dn9-0 RYkpI"})

print("Binance Coin: ")
print(price_bnb.text)
print(precent_bnb.text + " up/down" + "\n")


#Tether Stats
url_usdt = "https://coinmarketcap.com/currencies/tether/"
req = requests.get(url_usdt)
soup = BeautifulSoup(req.content, 'html.parser')
price_usdt = soup.find("div", {"class": "priceValue___11gHJ"})
precent_usdt = soup.find("span",{"class": "qe1dn9-0 RYkpI"})

print("Tether: ")
print(price_usdt.text)
print(precent_usdt.text + " up/down" + "\n")