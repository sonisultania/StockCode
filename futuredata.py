#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:37:52 2020

@author: sonisultania
"""

##Read Future contracts for a particular stock

import requests
import pandas as pd
from bs4 import BeautifulSoup 
import datetime
# for timezone() 
import pytz 


def futuredata(symbol):

    url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/fomwatchsymbol.jsp?key=' + symbol + '&Fut_Opt=Futures'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    
    # Load the page and sent to HTML parse
    page = requests.get(url,headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    futuretable = soup.find_all("div", {"class": "tabular_data_live_analysis"})
    
    futuretable = futuretable[0]
    
    dfs = pd.read_html(str(futuretable))
    df = dfs[0]
    
    futureheader = ['Instrument', 'Underlying', 'ExpiryDate', 'Option_Type', 'Strike_Price', 'Open',
                    'High_Price', 'Low_Price', 'Previous_Close', 'Last_Price', 'Volume', 
                    'Traded_Value', 'Underlying_Value']
    
    df.columns = futureheader
    
    df.loc[0,'Volume']
    return df