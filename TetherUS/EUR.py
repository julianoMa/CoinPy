# Import libraries
import json
import requests

# Defining Binance API URL
key = "https://api.binance.com/api/v3/ticker/price?symbol="

# Making list for multiple crypto's
currencies = ["USDTEUR"]
j = 0

# running loop to print all crypto prices
for i in currencies:

# completing API for request
 url = key+currencies[j]
data = requests.get(url)
data = data.json()
j = j+1
print("Le prix du TetherUS est de",data['price'],"€")