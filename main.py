from urllib.request import urlopen
import json


print("Ip info grabber :)")

# api request and gather info
address = input("Enter Ip: ")
req = f"http://api.ipstack.com/{address}?access_key=#"

respond = urlopen(req)

data = respond.read()
info = json.loads(data)

# present info
print("----------------------------------------------------------------------")
print("\n")
print("Ip:" + info['ip'])
print("Continent: " + info['continent_name'])
print("Country: " + info['country_name'])
print("City: " + info['city'])
print("Ip type: " + info['type'])
print("\n")
print("----------------------------------------------------------------------")
