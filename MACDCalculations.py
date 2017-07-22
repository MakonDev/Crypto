import numpy as np
import talib
from DataManipulation import split_raw_daily_data
from DataManipulation import split_raw_4hr_data
import matplotlib.pyplot as plt

dates, low_p, high_p, open_p, close_p, volume = split_raw_daily_data()
dates_4, low_p_4, high_p_4, open_p_4, close_p_4, volume_4 = split_raw_4hr_data()

def macd_calculation(close_p):
    macd, macdsignal, macdhist = talib.MACD(close_p, fastperiod=12, slowperiod=26, signalperiod=9)   
    return macd,macdsignal,macdhist

def detect_buy_sell_signals(macd, macdsignal, macdhist):
    num_buy_signals = 0
    num_sell_signals = 0
    buy = []
    sell = []
    for x in macdhist:
        if x > 0:
            num_buy_signals = num_buy_signals + 1
            buy.append(x)
        elif x < 0:
            num_sell_signals = num_sell_signals + 1
            sell.append(x)
        else:
            print("error it equals 0 or NAN!", x)
    print("Buy: ", num_buy_signals)
    print("Sell: ",num_sell_signals)
    return buy,sell

def detect_cross_signals(dates, macd, macdsignal, macdhist):
    cross_indices = []
    num_crosses = 0
    
    '''
    To get rid of Nan from not enough data in beginning to calc moving averages
    '''
    macd = np.delete(macd,np.s_[:33:],axis=None)
    macdsignal = np.delete(macdsignal,np.s_[:33:],axis=None)
    macdhist = np.delete(macd,np.s_[:33:],axis=None)
    dates = np.delete(dates,np.s_[:33:],axis=None)
    
    cross_indices = np.argwhere(np.diff(np.sign(macd - macdsignal)) != 0).reshape(-1) + 0
    num_crosses = len(cross_indices)
    
    print("num crosses: ",num_crosses)
    print("cross indices: ", cross_indices)
    return cross_indices,num_crosses



def detect_zero_crosses(macd, macdsignal, macdhist):
    
    
    return


def plot_macd(dates,macd,macdsignal,macdhist):
    '''
    To get rid of Nan from not enough data in beginning to calc moving averages
    '''
    macd = np.delete(macd,np.s_[:33:],axis=None)
    macdsignal = np.delete(macdsignal,np.s_[:33:],axis=None)
    macdhist = np.delete(macd,np.s_[:33:],axis=None)
    dates = np.delete(dates,np.s_[:33:],axis=None)
    
    plt.plot(dates,macd)
    plt.plot(dates,macdsignal)
    idx = np.argwhere(np.diff(np.sign(macd - macdsignal)) != 0).reshape(-1) + 0
    plt.plot(dates[idx], macd[idx], 'ro')
    plt.show()

    
    return "Done presenting"


def macd_backtest_crossover(dates,low_p,high_p,open_p,close_p,volume,macd,macdsignal,macdhist):
    
    '''Test theory that will profit from selling/buying on MACD crossover signals'''
    
    profit = 0
    profit_per_cross = []
   
    close_p = np.delete(close_p,np.s_[:33:],axis=None)

    cross_indices, num_crosses = detect_cross_signals(dates, macd, macdsignal, macdhist)
    
    
    for x in range(num_crosses+1):
        if x<51:
            index_new_p = cross_indices[x]
            index_old_p = cross_indices[x-1]
        
            new_p = close_p[index_new_p]
            old_p = close_p[index_old_p]
        
            curr_profit = ((new_p-old_p)/old_p)*100 #Percent change over period between buy & sell signal
            #print(curr_profit)
            profit = profit+curr_profit
            profit_per_cross.append(curr_profit)
        else:
            break
        
    #print("profit list: ", profit_per_cross)
    
    return profit
    
macd, macdsignal, macdhist = macd_calculation(close_p)
macd_4, macdsignal_4, macdhist_4 = macd_calculation(close_p_4)
profit = macd_backtest_crossover(dates,low_p,high_p,open_p,close_p,volume,macd,macdsignal,macdhist)
profit_4 = macd_backtest_crossover(dates_4,low_p_4,high_p_4,open_p_4,close_p_4,volume_4,macd_4,macdsignal_4,macdhist_4)
print("Profit (appx): ",profit,"%")
print("Profit 4 hours (appx): ",profit_4,"%")
#detect_buy_sell_signals(macd, macdsignal, macdhis)
#detect_cross_signals(dates,macd, macdsignal, macdhist)
plot_macd(dates,macd, macdsignal, macdhist)
plot_macd(dates_4,macd_4,macdsignal_4,macdhist_4)