# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:39:24 2016

@author: Administrator
"""

import tushare as ts
import pandas as pd 
import numpy as np

from pandas import DataFrame,Series


zz500s = ts.get_zz500s()

#==============================================================================
# for stock in zz500s['code']:
#     hisdata = ts.get_hist_data(stock,start ='20140101' )
#     hisdata.to_csv('D:\\pythonTest\\stockfile\\'+ stock +  '.csv' )
#==============================================================================

stocklist = []

for stock in zz500s['code']:
    hisdata = ts.get_hist_data(stock,start ='2016-04-01')
    
    if (abs(hisdata['close']-hisdata['ma5'])/hisdata['ma5']<0.02).all() \
    and (hisdata['ma5'] > hisdata['ma10']).all() \
    and (hisdata['ma10'] > hisdata['ma20']).all() \
    and (abs(hisdata['high']-hisdata['close'])/hisdata['close']<0.02).all():
       
       stocklist.append(stock)
       print stock
       
        
print stocklist