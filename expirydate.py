#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:59:42 2020

@author: sonisultania
"""

from datetime import datetime , timedelta


##Find last thursday of current month
def currentexpiry():
    todayte = datetime.today()
    todayte = todayte.replace(day=1)
    cmon = todayte.month
    
    nthu = todayte
    while todayte.month == cmon:
        todayte += timedelta(days=1)
        if todayte.weekday()==3: #this is Thursday 
            nthu = todayte
    
    currentexpiry = nthu.strftime("%d%b%Y").upper()
    return currentexpiry
    


##Find last thursday of next month
def nextexpiry():
    today = datetime.today()
    nextMonth = today + timedelta(days=31)
    nextMonth = nextMonth.replace(day=1)
    nextMonthmon = nextMonth.month
    
    sthu = nextMonth
    
    while nextMonth.month == nextMonthmon:
        nextMonth += timedelta(days=1)
        if nextMonth.weekday()==3: #this is Thursday 
            sthu = nextMonth
    
    nextexpiry = sthu.strftime("%d%b%Y").upper()
    return nextexpiry


