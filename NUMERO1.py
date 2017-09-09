#Importing Necessary Libraries
import urllib
import urllib2
import time
import hmac
import hashlib
import json
import requests
import csv
import pandas
try: 
    from openpyxl.cell import get_column_letter
except ImportError:
    from openpyxl.utils import get_column_letter


def Seducing():
	#Different API sources for different information
	#Trade Prices Conversions
	input1 = "https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-LTC"
	input2 = "https://bittrex.com/api/v1.1/public/getmarkethistory?market=ETH-OMG" 
	#Coin Market Summaries
	input3 = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc"
	input4 = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=eth-omg"
	
	#Pull API sources (Could implement loop here to be more elegant)
	requester1 = requests.get(input1)
	requester2 = requests.get(input2)
	requester3 = requests.get(input3)
	requester4 = requests.get(input4)
	
	#Massaging Funcion
	data1 = json.loads(requester1.text)
	data2 = json.loads(requester2.text)
	data3 = json.loads(requester3.text)
	data4 = json.loads(requester4.text)
	export1 = json.dumps(data1, sort_keys=True, indent=4)
	export2 = json.dumps(data2, sort_keys=True, indent=4)
	export3 = json.dumps(data3, sort_keys=True, indent=4)
	export4 = json.dumps(data4, sort_keys=True, indent=4)
	
	#Export BUYING and SELLING prices to EXCEL Function
	pandas.read_json(export1).to_excel("output.xlsx")
	
	#Execute Printing Function
	print "BTC to LTC Trade Prices:"
	print export1
	print "ETH to OMG Trade Prices:"
	print export2
	print "Below if the Following Market Prices of BTC to LTC:"
	print export3
	print "Below if the Following Market Prices of ETH to OMG:"
	print export4

Seducing()