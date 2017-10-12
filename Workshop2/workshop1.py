import urllib.request
import json
import csv

def dataCollect(start, end, exchange, currency1, currency2):
	data_bytes = urllib.request.urlopen("https://min-api.cryptocompare.com/data/histoday?fsym=" + str(currency1) + "&tsym=" + str(currency2) + "&limit="
		+ str(int((end - start) / 86400)) + "&toTs=" + str(end) + "&e=" + exchange).read()
	data_json = data_bytes.decode('utf8')
	data = json.loads(data_json)
	limit = len(data['Data'])
	actual_start = data['TimeFrom']
	actual_end = data['TimeTo']
	close_price = []
	high_price = []
	low_price = []
	open_price = []
	for i in range(limit):
		close_price.append(data['Data'][i]['close'])
		high_price.append(data['Data'][i]['high'])
		low_price.append(data['Data'][i]['low'])
		open_price.append(data['Data'][i]['open'])
	return close_price, high_price, low_price, open_price, actual_start, actual_end
	

def pricesCSV(start, prices):
	with open('file.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		length = len(prices)
		for i in range(length):
			writer.writerow([str(start + 86400 * i)] + [prices[i]])
