import numpy as np

def split_raw_daily_data():
    #determine number of daily values
    f = open("daily_candle_gdax_data.txt","r")
    num_days = 0 #counter for daily candles in data set
    for line in f:
        num_days+=1
    f.close()
    print("Number of candles: ",num_days)
    
    #create numpy arrays to house different candlestick values
    #need to be same sizes!!
    dates = np.empty(num_days,)
    low_p = np.empty(num_days,)
    high_p = np.empty(num_days,)
    open_p = np.empty(num_days,)
    close_p = np.empty(num_days,)
    volume = np.empty(num_days,)

    
    #import dat from text file
    f = open("daily_candle_gdax_data.txt", "r")
    i=0 #counter for row placement into array
    for line in f:
        line = line.strip("\n") #strips \n from end of each line
        line = line.strip("]") #strips \n from end of each line
        line = line.strip("[") #strips \n from end of each line
        j=0 #counter for each array placement
        for word in line.split(","): #splits line into individual items by ","
            #print(word)
            if j==0: #date in unix time
                dates[i] = int(word)
            elif j==1: #if low price
                low_p[i] = float(word)
            elif j==2: #if high price
                high_p[i] = float(word)
            elif j==3: #if open price
                open_p[i] = float(word)
            elif j==4: #if close price
                close_p[i] = float(word)
            elif j==5: #if volume
                volume[i] = float(word)
            else: #none of these so an error
                return "Uh oh! Error setting daily data to their arrays!"                                
            j=j+1
        i=i+1
        
    f.close()
    
    
    

    dates = dates.astype(int)
    #print("dates: ",dates)
    #print("low_p: ",low_p)
    #print("high_p: ",high_p)
    #print("open_p: ",open_p)
    #print("close_p: ",close_p)
    #print("volume: ",volume)
    
    return dates, low_p, high_p, open_p, close_p, volume


def split_raw_4hr_data():
    #determine number of daily values
    f = open("4hr_candle_gdax_data.txt","r")
    num_candles = 0 #counter for daily candles in data set
    for line in f:
        num_candles+=1
    f.close()
    print("Number of candles: ",num_candles)
    
    #create numpy arrays to house different candlestick values
    #need to be same sizes!!
    dates = np.empty(num_candles,)
    low_p = np.empty(num_candles,)
    high_p = np.empty(num_candles,)
    open_p = np.empty(num_candles,)
    close_p = np.empty(num_candles,)
    volume = np.empty(num_candles,)

    #import dat from text file
    f = open("4hr_candle_gdax_data.txt", "r")
    i=0 #counter for row placement into array
    for line in f:
        line = line.strip("\n") #strips \n from end of each line
        line = line.strip("]") #strips \n from end of each line
        line = line.strip("[") #strips \n from end of each line
        j=0 #counter for each array placement
        for word in line.split(","): #splits line into individual items by ","
            #print(word)
            if j==0: #date in unix time
                dates[i] = int(word)
            elif j==1: #if low price
                low_p[i] = float(word)
            elif j==2: #if high price
                high_p[i] = float(word)
            elif j==3: #if open price
                open_p[i] = float(word)
            elif j==4: #if close price
                close_p[i] = float(word)
            elif j==5: #if volume
                volume[i] = float(word)
            else: #none of these so an error
                return "Uh oh! Error setting 4 hr data to their arrays!"                                
            j=j+1
        i=i+1
        
    f.close()
    
    return dates, low_p, high_p, open_p, close_p, volume
#split_raw_daily_data()