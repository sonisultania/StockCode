#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:25:40 2020

@author: sonisultania
"""
#Create daily NSE option data for a list of stocks
import requests
import pandas as pd
from bs4 import BeautifulSoup 
import datetime
import re #regex module
# for timezone() 
import pytz 

current_time = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))  
current_day = current_time.day
current_month = current_time.strftime("%b")
current_hour = current_time.hour

path1 = '/Users/sonisultania/Desktop/Python/OIDaily/NIFTYACTIVE.csv'
NIFTY = pd.read_csv(path1, header = None)

NIFTY.columns = ['NIFTY']


symbollist = NIFTY['NIFTY']

for stock in symbollist:
    
    symbol = stock
    expiry = '26MAR2020'
#Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=-"
    
    Base_url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&instrument=OPTSTK&symbol=" + symbol + "&date=" + expiry

#    Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=-"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    # Load the page and sent to HTML parse
    page = requests.get(Base_url,headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    optiontable = soup.find_all("div", {"class": "opttbldata"})
    optiontable = optiontable[0]

    dfs = pd.read_html(str(optiontable))
    df = dfs[0]

    optionheader = ['CCHART','COI', 'CCHANGE', 'CVOLUME', 'CIV', 'CLTP', 'CNETC', 'CBIDQ', 'CBIDP', 'CASKP', 'CASKQ', 
                    'STRIKEP',
                    'PBIDQ', 'PBIDP', 'PASKP', 'PASKQ', 'PNETC', 'PLTP', 'PIV', 'PVOLUME', 'PCHANGE', 'POI', 'PCHART']

    df.columns = optionheader

    df.drop(['CCHART', 'PCHART', 'CBIDQ', 'PBIDQ', 'CASKQ', 'PASKQ', 'CBIDP', 'CASKP' , 'PBIDP', 'PASKP' ], axis = 1, inplace = True)

    df.replace('-', '0', inplace = True)

    df = df.apply(pd.to_numeric) #convert all columns to numeric

    df = df[:-1] #drop the last row

    df['PCR'] = df['POI']/df['COI'] #add a new PCR column
    
    tags = soup('span')
    String = tags[1].text
    
    res = re.findall(r'\w+', String) 
    
    day = res[3]
    month = res[2]
    hour = res[5]
    
    path2 = '/Users/sonisultania/Desktop/Python/OIdaily/dailycsv/'
    
    filename  = symbol + day + month + hour + '.csv'
    
    file = path2 + filename
    
    df.to_csv(file, index = False)  #Write files

