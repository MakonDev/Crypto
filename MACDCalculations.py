import numpy as np
import matplotlib.pyplot as plt
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
    
    #print("num crosses: ",num_crosses)
    #print("cross indices: ", cross_indices)
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
    durations = []
    
    close_p = np.delete(close_p,np.s_[:33:],axis=None)

    cross_indices, num_crosses = detect_cross_signals(dates, macd, macdsignal, macdhist)
    
    
    for x in range(num_crosses+1):
        if x<num_crosses:
            index_new_p = cross_indices[x]
            index_old_p = cross_indices[x-1]
            
            duration = index_new_p - index_old_p
            durations.append(duration)
        
            new_p = close_p[index_new_p]
            old_p = close_p[index_old_p]
        
            curr_profit = ((new_p-old_p)/old_p)*100 #Percent change over period between buy & sell signal
            #print(curr_profit)
            profit = profit+curr_profit
            profit_per_cross.append(curr_profit)
        else:
            break
        
    #print("profit list: ", profit_per_cross)
    
    
    
    
    return profit, profit_per_cross, durations
    
    
    
def consolidate_results(profit,profit_per_cross,durations):
    if len(profit_per_cross)!=len(durations):
        return "Error in profit/duration data collection"
        #means not enough durations for crosses, indicates that something went wrong collecting this data
    results = np.empty((len(profit_per_cross),2))
    for i in range(len(profit_per_cross)):
        results[i][0] = float(profit_per_cross[i])
        results[i][1] = int(durations[i])
    
    
    return results

def plot_histogram(results):
    
    duration = np.empty((len(results),))
                        
    for i in range(len(results)):
        if i==0:
            print("do nothing") #BC first one has weird values
        else:
            duration[i] = results[i][1]
    
    plt.hist(duration,50)
    plt.title("Duration Histogram")
    plt.xlabel("Duration")
    plt.ylabel("Frequency")
    plt.show()
    
    return "Histogram Finished"

def backtest_duration_limit(dates,low_p,high_p,open_p,close_p,volume,macd,macdsignal,macdhist):
    '''Test theory that will profit from selling/buying on MACD crossover signals but only on ones longer than x days'''
    duration_limit = 5
    profit = 0
    profit_per_cross = []
    durations = []
    
    close_p = np.delete(close_p,np.s_[:33:],axis=None)

    cross_indices, num_crosses = detect_cross_signals(dates, macd, macdsignal, macdhist)
    
    
    for x in range(num_crosses+1):
        if x<num_crosses:
            index_new_p = cross_indices[x]
            index_old_p = cross_indices[x-1]
            duration = index_new_p - index_old_p
            if duration > duration_limit:
       
                durations.append(duration)
        
                new_p = close_p[index_new_p]
                old_p = close_p[index_old_p]
        
                curr_profit = ((new_p-old_p)/old_p)*100 #Percent change over period between buy & sell signal
                #print(curr_profit)
                profit = profit+curr_profit
                profit_per_cross.append(curr_profit)
            else:
                continue
        else:
            break
        
    #print("profit list: ", profit_per_cross)
    
    
    
    
    return profit, profit_per_cross, durations
#format future float printouts
float_formatter = lambda x: "%.3f" % x
np.set_printoptions(formatter={'float_kind':float_formatter})




macd, macdsignal, macdhist = macd_calculation(close_p)
macd_4, macdsignal_4, macdhist_4 = macd_calculation(close_p_4)

'''
#Test strategy & results without limit on duration

profit, profit_per_cross, durations = macd_backtest_crossover(dates,low_p,high_p,open_p,close_p,volume,macd,macdsignal,macdhist)
profit_4, profit_per_cross_4, durations_4 = macd_backtest_crossover(dates_4,low_p_4,high_p_4,open_p_4,close_p_4,volume_4,macd_4,macdsignal_4,macdhist_4)

print("Profit (appx): ",profit,"%")
print("Duration per cross: ",durations)
print("Profit 4 hours (appx): ",profit_4,"%")
print("Duration per 4 hr cross: ",durations_4)

results = consolidate_results(profit, profit_per_cross, durations)
results_4hr = consolidate_results(profit_4, profit_per_cross_4, durations_4)

print("daily results: ", results)
print("4 hr results: ", results_4hr)
plot_histogram(results)
plot_histogram(results_4hr)
#plot_macd(dates,macd, macdsignal, macdhist)
#plot_macd(dates_4,macd_4,macdsignal_4,macdhist_4)
'''
#Test strategy with duration limit

profit_l, profit_per_cross_l, durations_l = backtest_duration_limit(dates,low_p,high_p,open_p,close_p,volume,macd,macdsignal,macdhist)
profit_4_l, profit_per_cross_4_l, durations_4_l = backtest_duration_limit(dates_4,low_p_4,high_p_4,open_p_4,close_p_4,volume_4,macd_4,macdsignal_4,macdhist_4)
print("Profit (appx): ",profit_l,"%")
print("Duration per cross: ",durations_l)
print("Profit 4 hours (appx): ",profit_4_l,"%")
print("Duration per 4 hr cross: ",durations_4_l)
results_l = consolidate_results(profit_l, profit_per_cross_l, durations_l)
results_4hr_l = consolidate_results(profit_4_l, profit_per_cross_4_l, durations_4_l)
#print("daily results: ", results_l)
#print("4 hr results: ", results_4hr_l)
plot_histogram(results_l)
plot_histogram(results_4hr_l)

#plot_macd(dates,macd, macdsignal, macdhist)
#plot_macd(dates_4,macd_4,macdsignal_4,macdhist_4)
