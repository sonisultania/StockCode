#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:16:30 2020
This Program finds the Average True Range for Stocks for last 5 days
@author: sonisultania
"""

import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
#import fix_yahoo_finance
import pandas as pd
import csv

enddate = '2020-03-20'
startdate = '2020-03-05'

path1 = '/Users/sonisultania/Desktop/Python/OIDaily/NIFTY50.csv'

NIFTY = pd.read_csv(path1, header = None)

NIFTY.columns = ['NIFTY']

NIFTY = NIFTY + '.NS'

df = pd.DataFrame()
atr = pd.DataFrame()

symbollist = NIFTY['NIFTY']
#symbollist = ['BIOCON.NS', 'BATAINDIA.NS', 'POWERGRID.NS', 'PFC.NS', 'RECLTD.NS']

for stock in symbollist:   
    symbol = stock
    data = pdr.get_data_yahoo(stock, start=startdate, end=enddate) 
    df['ATR'] = data['High'].subtract(data['Low']).rolling(5).mean()  
    df['ATRPCT'] = df['ATR']/data['Close']
    df['Stock'] = stock
    avgatr = df.iloc[-5]['ATRPCT'].mean()
    d1 = {'Stock': stock, 'AVGATR': avgatr}
    atr = atr.append(d1, ignore_index=True)
    
#atr[atr.AVGATR == atr.AVGATR.max()]