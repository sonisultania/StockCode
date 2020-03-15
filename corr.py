#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:53:45 2020

@author: sonisultania
"""

import numpy as np
import pandas as pd
#used to grab the stock prices, with yahoo
import pandas_datareader as web
from datetime import datetime
#to visualize the results
import matplotlib.pyplot as plt
import seaborn
 
#select start date for correlation window as well as list of tickers
start = datetime(2016,1,1)

#symbols_list = ['CADILAHC.NS', 'BIOCON.NS', 'AMBUJACEM.NS']


#List = ['YESBANK', 'KOTAKBANK', 'RBLBANK','IDFCFIRSTB', 'SBIN',	'PNB',	
#           'INDUSINDBK','BANKBARODA','HDFCBANK',	'FEDERALBNK', 'AXISBANK', 'ICICIBANK']

#List = ['^NSEI', '^HSI', '^N225', '^DJI']
List = ['TATAPOWER.NS', 'ONGC.NS', 'PFC.NS', 'RECLTD.NS']
#s = '.NS'
#
#symbols_list = ["{}{}".format(i,s) for i in List]

#Pull stock prices, push into clean dataframe

#array to store prices
symbols=[]

#pull price using iex for each symbol in list defined above
for ticker in List: 
    r = web.DataReader(ticker, 'yahoo', start)
    # add a symbol column
    r['Symbol'] = ticker 
    symbols.append(r)

# concatenate into df
df = pd.concat(symbols)
df = df.reset_index()
df = df[['Date', 'Close', 'Symbol']]
df.head()

df_pivot = df.pivot('Date','Symbol','Close').reset_index()
df_pivot.head()

corr_df = df_pivot.corr(method='pearson')
#reset symbol as index (rather than 0-X)
corr_df.head().reset_index()
del corr_df.index.name
corr_df.head(12)

#take the bottom triangle since it repeats itself
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
#generate plot
seaborn.heatmap(corr_df, cmap='RdYlGn', vmax=1.0, vmin=-1.0 , mask = mask, linewidths=2.5)
plt.yticks(rotation=0) 
plt.xticks(rotation=90) 
plt.show()
