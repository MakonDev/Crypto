import numpy as np
import matplotlib.pyplot as plt
import talib
from DataManipulation import split_raw_daily_data
from DataManipulation import split_raw_4hr_data
import matplotlib.pyplot as plt

'''
dates, low_p, high_p, open_p, close_p, volume = split_raw_daily_data()
dates_4, low_p_4, high_p_4, open_p_4, close_p_4, volume_4 = split_raw_4hr_data()
'''

def calc_RSI(close):
    real = talib.RSI(close, timeperiod=14)
    return real

def ob_ub(dates,rsi_list):
    overbought = 0
    underbought = 0
    ob_dates = []
    ub_dates= []
    for i in range(len(rsi_list)):
        if rsi_list[i]>70:
            overbought+=1
            ob_dates.append(dates[i])
            j=+1
        elif rsi_list[i]<30:
            underbought+=1
            ub_dates.append(dates[i])
            b=+1
        else:
            pass
    return overbought,underbought,ob_dates,ub_dates
  
'''
RSI_list = calc_RSI(close_p)
overbought,underbought,ob_dates,ub_dates = ob_ub(dates,RSI_list)
print(overbought,underbought)
print(ob_dates)
print(ub_dates)
'''