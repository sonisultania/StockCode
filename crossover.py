#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:25:59 2020

@author: sonisultania
"""

import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
#import fix_yahoo_finance
import pandas as pd
import csv
from itertools import zip_longest


stock = 'BIOCON.NS'
data = pdr.get_data_yahoo(stock, start="2018-01-01", end="2020-03-07") 

data['Close'].plot(grid = True)
plt.title("HCLTECH Closing Prices")
plt.show()

df = data[['Close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']

exp50 = df.y.ewm(span=50, adjust=False).mean()
exp200 = df.y.ewm(span=200, adjust=False).mean()


short_window = 50
long_window = 100

signals = pd.DataFrame(index=data.index)

signals['signal'] = 0.0

signals['EMA50'] = exp50.values
signals['EMA200'] = exp200.values

signals['signal'][short_window:] = np.where(signals['EMA50'][short_window:] 
                                    > signals['EMA200'][short_window:], 1.0, 0.0)

signals['positions'] = signals['signal'].diff()

fig = plt.figure(figsize=(20,15))
ax1 = fig.add_subplot(111, ylabel = 'Price in Rs')
#Plot the closing price

data['Close'].plot(ax=ax1, color = 'black', lw=2.)

signals[['EMA50', 'EMA200']].plot(ax=ax1, lw=2.)

##Plot the buy signals

ax1.plot(signals.loc[signals.positions == 1.0].index,
         signals.EMA50[signals.positions == 1.0],
        '^', markersize = 20, color ='g')

ax1.plot(signals.loc[signals.positions == -1.0].index,
         signals.EMA50[signals.positions == 1.0],
        '^', markersize = 20, color ='g')

#Show the plot

#plt.show()

plt.savefig('ssonni.png')

                                    



