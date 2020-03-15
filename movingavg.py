#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:51:50 2020

@author: sonisultania
"""

import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
#import fix_yahoo_finance
import pandas as pd
import csv
from itertools import zip_longest

emadate = '2020-03-03'
emaprev = '2020-02-28'
#Read NIFTY50 file

in50ema = []
in200ema = []
broke50ema =[]
h50emabroke = []
cross50ema = []
cross200ema= []


path1 = '/Users/sonisultania/Desktop/Python/OIDaily/NEXT50.csv'

NIFTY = pd.read_csv(path1, header = None)

NIFTY.columns = ['NIFTY']

NIFTY = NIFTY + '.NS'

symbollist = NIFTY['NIFTY']

for stock in symbollist:   
    symbol = stock
    data = pdr.get_data_yahoo(stock, start="2019-01-01", end="2020-03-03") 
    
    df = data[['Close']]
    df.reset_index(level=0, inplace=True)
    df.columns=['ds','y']
    
    exp50 = df.y.ewm(span=50, adjust=False).mean()
    exp200 = df.y.ewm(span=200, adjust=False).mean()
    data['EMA50'] = exp50.values
    data['EMA200'] = exp200.values
    
#    if (data[emadate:emadate]['Close'] > data[emadate:emadate]['EMA50']).all():
#        print(stock)
#        in50ema.append(stock)
#        
#    if (data[emadate:emadate]['Close'] > data[emadate:emadate]['EMA200']).all():
#        in200ema.append(stock)
#        
##        
#    if (data[emaprev:emaprev]['Close'].values < data[emadate:emadate]['EMA200'].values).all():
#        if (data[emadate:emadate]['Close'] > data[emadate:emadate]['EMA200']).all():
#            print('Broke yday, recovered today')
##            broke50ema.append(stock)
#            cross200ema.append(stock)
    
    if (data[emadate:emadate]['High'] > data[emadate:emadate]['EMA50']).all():
        if (data[emadate:emadate]['Close'] < data[emadate:emadate]['EMA50']).all():
            h50emabroke.append(stock)
#    
    
#    if (data[emadate:emadate]['Low'] < data[emadate:emadate]['EMA50']).all():
#        if (data[emadate:emadate]['Close'] > data[emadate:emadate]['EMA50']).all():
##    
#    
##    if (data[emadate:emadate]['Low'] < data[emadate:emadate]['EMA200']).all():
#        if (data[emadate:emadate]['Close'] > data[emadate:emadate]['EMA200']).all():
#            print(stock)
#               
               
d = [in50ema, in200ema, broke50ema, h50emabroke]

export_data = zip_longest(*d, fillvalue = '')
with open('NEXT50.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("in50ema", "in200ema", "broke50ema", "h50emabroke"))
      wr.writerows(export_data)
myfile.close()        
    

    
    