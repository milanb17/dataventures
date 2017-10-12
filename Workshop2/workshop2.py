
from workshop1 import dataCollect
import numpy as np
import matplotlib.pyplot as plt
import csv
from math import log
def linearPred():
	time = []
	rate = []
	with open('close.csv', 'rt') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			time.append(float(row[0]))
			rate.append(float(row[1]))
	
	time_15 = time[0:15]
	rate_15 = rate[0:15]
	fit = np.polyfit(time_15,rate_15,1)
	fit_fn = np.poly1d(fit) 
	plt.plot(time_15,rate_15, 'yo', time, fit_fn(time), '--k')
	plt.xlim(1504200000, 1506800000)
	plt.ylim(0.06, 0.08)
	plt.show()

	sd = 0.0
	mean = 0.0
	rate_15_30 = rate[15:30]
	pred_15_30 = fit_fn(time[15:30])
	for i in range(len(rate_15_30)):
		sd += (rate_15_30[i] - pred_15_30[i]) ** 2
		mean += rate_15_30[i]
	mean = mean / len(rate_15_30)
	sd = (sd / len(rate_15_30)) ** (1/2.0)
	print(sd / mean) #relative standard deviation

#########################################################################################################################33
	sqrt_time = []
	for i in range(len(time)):
		sqrt_time.append(time[i] ** (1/2.0))
	sqrt_time_15 = sqrt_time[0:15]
	rate_15 = rate[0:15]
	fit = np.polyfit(sqrt_time_15,rate_15,1)
	fit_fn = np.poly1d(fit) 
	plt.plot(sqrt_time,rate, 'yo', sqrt_time, fit_fn(sqrt_time), '--k')
	plt.xlim(1504200000 ** (1/2.0), 1506800000 ** (1/2.0))
	plt.ylim(0.06, 0.08)
	plt.show()

	sqrt_sd = 0.0
	sqrt_mean = 0.0
	rate_15_30 = rate[15:30]
	sqrt_pred_15_30 = fit_fn(sqrt_time[15:30])
	for i in range(len(rate_15_30)):
		sd += (rate_15_30[i] - sqrt_pred_15_30[i]) ** 2
		mean += rate_15_30[i]
	mean = mean / len(rate_15_30)
	sd = (sd / len(rate_15_30)) ** (1/2.0)
	print(sd / mean) #relative standard deviation




