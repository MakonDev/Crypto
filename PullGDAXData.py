import numpy as np
import gdax
import json
import dateutil.parser as parser
import calendar
import pytz
from datetime import datetime
import requests

num_daily_candles=0
num_4hr_candles=0
day_unix_times= []

### Data pulled from GDAX web API ###

#Data begins from 1-8-15 thru present (as close as possible)
def get_gdax_historical_data():

    data = []
    public_client = gdax.PublicClient() #creates public client object
    #bit_usd_stats = public_client.get_product_historic_rates('BTC-USD',"2017-07-08T00:00:00+00:00","2017-07-08T16:40:00+00:00",granularity=300)
    #print(bit_usd_stats)
    
    
    #create loops to generate historical data queries from GDAX
    #parse for 4 hr data
    '''
    calendar_class = calendar.Calendar(6) #Creates calendar w/ weeks starting on sundays
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    years = [2015,2016,2017]
    for year in years:
        for month in months:
            if year == 2017 and month > 6: #since in july, 2017 we'll handle this specifically 
                    break
            print("Month, Year: ", month, year)
            for day in calendar_class.itermonthdays2(year,month):
                if day[0]>0: #if not day of another month that's just included in a given week due to calendar formatting
                       # text1 = ""+year+"-"+month+"-"+day[0]+"T"+"00:00:00 +0000"
                        #print(text1)
    #Correct ISO format = 2017-07-11T18:10:00+04:00
    '''
    
    
    
    
    
    
    
    #collect daily data and store in text file
    

    file = open("daily_candle_gdax_data.txt","w")
    #Eventually write script to automate, but for now list out all groupings just for expediency in groups of 200, then remaining
    #dates = ["2015-01-01T00:00:00+00:00","2015-05-04T00:00:00+00:00","2015-11-20T00:00:00+00:00","2016-06-07T00:00:00+00:00","2016-12-24T00:00:00+00:00","2017-07-12T00:00:00+00:00"]
    bit_usd_stats1 = public_client.get_product_historic_rates('BTC-USD',"2015-01-01T00:00:00+00:00","2015-05-04T00:00:00+00:00",granularity=86400)
    global num_daily_candles
    num_daily_candles = num_daily_candles + len(bit_usd_stats1)
    bit_usd_stats1=sorted(bit_usd_stats1,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats1)):
        file.write(str(bit_usd_stats1[x])+"\n")
        global day_unix_times
        day_unix_times.append(bit_usd_stats1[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats1)) #200 days/pts exactly from 7/11/17 back thru 12/24/16,then 12/23/16 - 6/7/16, then (other dates and so on but 111 until 1/1/15 which is chosen start date for GDAX data
    #print(bit_usd_stats1)
    bit_usd_stats1.reverse()
    #print(bit_usd_stats1)
    data.append(bit_usd_stats1)
    
    
    bit_usd_stats2 = public_client.get_product_historic_rates('BTC-USD',"2015-05-04T00:00:00+00:00","2015-11-20T00:00:00+00:00",granularity=86400)
    #global num_daily_candles
    num_daily_candles = num_daily_candles + len(bit_usd_stats2)
    bit_usd_stats2=sorted(bit_usd_stats2,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats2)):
        file.write(str(bit_usd_stats2[x])+"\n") 
        day_unix_times.append(bit_usd_stats2[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats2)) 
    #print(bit_usd_stats2)
    bit_usd_stats2.reverse()
    #print(bit_usd_stats2)
    data.append(bit_usd_stats2)
    
    
    bit_usd_stats3 = public_client.get_product_historic_rates('BTC-USD',"2015-11-20T00:00:00+00:00","2016-06-07T00:00:00+00:00",granularity=86400)
    #global num_daily_candles
    num_daily_candles = num_daily_candles + len(bit_usd_stats3)
    bit_usd_stats3=sorted(bit_usd_stats3,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats3)):
        file.write(str(bit_usd_stats3[x])+"\n") 
        day_unix_times.append(bit_usd_stats3[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats3))
    #print(bit_usd_stats3)
    bit_usd_stats3.reverse()
    #print(bit_usd_stats3)
    data.append(bit_usd_stats3)

    
    bit_usd_stats4 = public_client.get_product_historic_rates('BTC-USD',"2016-06-07T00:00:00+00:00","2016-12-24T00:00:00+00:00",granularity=86400)
    #global num_daily_candles
    num_daily_candles = num_daily_candles + len(bit_usd_stats4)
    bit_usd_stats4=sorted(bit_usd_stats4,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats4)):
        file.write(str(bit_usd_stats4[x])+"\n")  
        day_unix_times.append(bit_usd_stats4[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats4)) 
    #print(bit_usd_stats4)
    bit_usd_stats4.reverse()
    #print(bit_usd_stats4)
    data.append(bit_usd_stats4)
    
    
    bit_usd_stats5 = public_client.get_product_historic_rates('BTC-USD',"2016-12-24T00:00:00+00:00","2017-07-12T00:00:00+00:00",granularity=86400)
    #global num_daily_candles
    num_daily_candles = num_daily_candles + len(bit_usd_stats5)
    bit_usd_stats5=sorted(bit_usd_stats5,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats5)):
        file.write(str(bit_usd_stats5[x])+"\n")
        day_unix_times.append(bit_usd_stats5[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats5)) 
    bit_usd_stats5.reverse()
    data.append(bit_usd_stats5)

    
    #add daily data to the overall list to still account for passing days
    
    bit_usd_stats = public_client.get_product_historic_rates('BTC-USD',"2017-07-12T00:00:00+00:00","2017-07-20T00:00:00+00:00",granularity=86400) #go from date range of [last date entered]-[current date]
    bit_usd_stats=sorted(bit_usd_stats,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats)):
        if x==(len(bit_usd_stats)-1):
            file.write(str(bit_usd_stats[x]))
        else:
            file.write(str(bit_usd_stats[x])+"\n")
        day_unix_times.append(bit_usd_stats[x][0])
    bit_usd_stats.reverse()
    data.append(bit_usd_stats)
    file.close()
    
    #write unix days to file
    f1 = open("day_unix_times.txt","w")
    for x in range(len(day_unix_times)):
        if x==(len(day_unix_times)-1):
            f1.write(str(day_unix_times[x]))
        else:
            f1.write(str(day_unix_times[x])+"\n")
    f1.close()
    return data


get_gdax_historical_data()
