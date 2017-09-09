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
import xlsxwriter
#try: 
#    from openpyxl.cell import get_column_letter
#except ImportError:
#    from openpyxl.utils import get_column_letter


def Seducing():
	#Different API sources for different information
	#Trade Prices Conversions
	input1 = "https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-OMG"
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
	
	#print export1
	
	#arraynum = data1.rows
	
	#writer 
	i=0
	j=0
	m=0
	
	#Loop to seperate data into arrays
	# for rows in data1['result']:
		# writer[i][j] = rows['FillType']
		# writer[i][j+1] = rows['ID']
		# writer[i][j+2] = rows['OrderType']
		# writer[i][j+3] = rows['Price']
		# writer[i][j+4] = rows['Quantity']
		# writer[i][j+5] = rows['TimeStamp']
		# writer[i][j+6] = rows['Total']
		# i=i+1
	
	#Export BUYING and SELLING prices to EXCEL Function
	workbook = xlsxwriter.Workbook('Export3.xlsx')
	worksheet = workbook.add_worksheet()
	
	worksheet.write('A1', 'FillType')
	worksheet.write('B1', 'Id')
	worksheet.write('C1', 'OrderType')
	worksheet.write('D1', 'Price')
	worksheet.write('E1', 'Quantity')
	worksheet.write('F1', 'TimeStamp')
	worksheet.write('G1', 'Total')
	
	i=1
	for rows in data1['result']:
		worksheet.write('A'+str(i+1),rows['FillType'])#writer[i][j])
		worksheet.write('B'+str(i+1),rows['Id'])#writer[i][j+1])
		worksheet.write('C'+str(i+1),rows['OrderType'])#writer[i][j+2])
		worksheet.write('D'+str(i+1),rows['Price'])#writer[i][j+3])
		worksheet.write('E'+str(i+1), rows['Quantity'])#writer[i][j+4])
		worksheet.write('F'+str(i+1),rows['TimeStamp'])#writer[i][j+5])
		worksheet.write('G'+str(i+1),rows['Total'])#writer[i][j+6])
		i=i+1
	
	
	#Execute Printing Function
	#print "BTC to LTC Trade Prices:"
	#print export1
	#print "ETH to OMG Trade Prices:"
	#print export2
	#print "Below if the Following Market Prices of BTC to LTC:"
	#print export3
	#print "Below if the Following Market Prices of ETH to OMG:"
	#print export4

Seducing()