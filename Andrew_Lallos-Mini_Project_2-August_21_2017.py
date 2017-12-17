
# Andrew Lallos
# WorldQuant University
# WQU607 - Algorithms 1
# Mini Project 2, due August 21st, 2017

import numpy as np
from pylab import *
import scipy.signal as sc
from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')
import pandas_datareader.data as web
import datetime

# set our start and end dates for our analysis
# A two year period between 12/2013 and 12/2015 has been chosen

start = datetime.datetime(2013, 12, 6)
end = datetime.datetime(2015, 12, 20)

# Download our data

oil = web.DataReader("WTI", data_source='quandl', start = start, end= end)
oil = oil.AdjClose
plt.plot(oil)
plt.title("Crude Oil Prices, 12/2013 - 12/2015")

# Detrending our data

detrend = sc.detrend(oil)
plt.plot(detrend)
plt.title("Detrend Oil Data")

# Apply the Blackman window function

w=np.blackman(20) #we selected 20 the parameter of the blackman window function
y=np.convolve(w/w.sum(),detrend,mode='same')
plt.plot(y)
plt.title("‘Blackman window function for detrended Crude Oil price’")

# Run the FFT algorithm on our data

fft = abs(rfft(y))
plt.plot(fft)
plt.title("‘FFT Algorithm applied to Crude Oil price’")

# Adjust the scale to more easily see cycles

plt.plot(fft)
plt.axis(xmin = 0, xmax = 50)
plt.title("‘FFT Algorithm applied to Crude Oil price, Limit 50’")


print(fft)



