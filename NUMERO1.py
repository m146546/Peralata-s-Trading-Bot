#Importing Necessary Libraries
import urllib
import urllib2
import time
import hmac
import hashlib
import json
import requests

def Seducing():
	#importing coin data
	requester = requests.get("https://bittrex.com/api/v1.1/public/getmarkets")

	data = requester.json()
	
	print(requester.headers["content-type"])

Seducing()