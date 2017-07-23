import numpy as np
import gdax
import json
import dateutil.parser as parser
import calendar
import pytz
from datetime import datetime
import requests


#global variables
num_daily_candles = 0
num_4hr_candles = 0
day_unix_times = []
fourhr_unix_times = []


### Data pulled from GDAX web API ###
'''
Date requests in ISO8601 format, and they're in GMT, not EST, so 5pm GMT = 1pm EST
Disclaimer: If try to pull a request with an end date for a time that is in the future, even by a minute, will cause strange behavior in data that's pulled! Only stay current up to most recent hour
'''

#Data begins from 1-8-15 thru present (as close as possible)
def get_gdax_historical_data():

    daily_data = []
    fourhr_data = []
    public_client = gdax.PublicClient() #creates public client object
    
    
    
    #collect 4hr data and store in text file
    #parse for 4 hr data
    
    file = open("4hr_candle_gdax_data.txt","w")
    #collect 4hr chart data on a monthly basis for easy tracking of data correctness
    
    #holds all month beginning dates to use as start and end of "get" api requests
    #beg_end_months = ["2015-01-01T00:00:00+00:00","2015-02-01T00:00:00+00:00","2015-03-01T00:00:00+00:00","2015-04-01T00:00:00+00:00","2015-05-01T00:00:00+00:00","2015-06-01T00:00:00+00:00","2015-07-01T00:00:00+00:00","2015-08-01T00:00:00+00:00","2015-09-01T00:00:00+00:00","2015-10-01T00:00:00+00:00","2015-11-01T00:00:00+00:00","2015-12-01T00:00:00+00:00","2016-01-01T00:00:00+00:00","2016-02-01T00:00:00+00:00","2016-03-01T00:00:00+00:00","2016-04-01T00:00:00+00:00","2016-05-01T00:00:00+00:00","2016-06-01T00:00:00+00:00","2016-07-01T00:00:00+00:00","2016-08-01T00:00:00+00:00","2016-09-01T00:00:00+00:00","2016-10-01T00:00:00+00:00","2016-11-01T00:00:00+00:00","2016-12-01T00:00:00+00:00","2017-01-01T00:00:00+00:00","2017-02-01T00:00:00+00:00","2017-03-01T00:00:00+00:00","2017-04-01T00:00:00+00:00","2017-05-01T00:00:00+00:00","2017-06-01T00:00:00+00:00","2017-07-01T00:00:00+00:00","2017-08-01T00:00:00+00:00"]
    
    global num_4hr_candles
    global fourhr_unix_times
    
    '''
    Month by month static retrieval of historical 4hr candle chart data, saved in text file so 
    this doesn't have to be called continuously and take up time, nor require internet connection to run/edit other files
    '''
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-01-01T00:00:00+00:00","2015-02-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-02-01T00:00:00+00:00","2015-03-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-03-01T00:00:00+00:00","2015-04-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-04-01T00:00:00+00:00","2015-05-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-05-01T00:00:00+00:00","2015-06-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-06-01T00:00:00+00:00","2015-07-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-07-01T00:00:00+00:00","2015-08-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-08-01T00:00:00+00:00","2015-09-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-09-01T00:00:00+00:00","2015-10-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-10-01T00:00:00+00:00","2015-11-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-11-01T00:00:00+00:00","2015-12-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2015-12-01T00:00:00+00:00","2016-01-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-01-01T00:00:00+00:00","2016-02-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-02-01T00:00:00+00:00","2016-03-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-03-01T00:00:00+00:00","2016-04-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-04-01T00:00:00+00:00","2016-05-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-05-01T00:00:00+00:00","2016-06-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-06-01T00:00:00+00:00","2016-07-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-07-01T00:00:00+00:00","2016-08-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-08-01T00:00:00+00:00","2016-09-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-09-01T00:00:00+00:00","2016-10-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-10-01T00:00:00+00:00","2016-11-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-11-01T00:00:00+00:00","2016-12-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2016-12-01T00:00:00+00:00","2017-01-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2017-01-01T00:00:00+00:00","2017-02-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2017-02-01T00:00:00+00:00","2017-03-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2017-03-01T00:00:00+00:00","2017-04-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2017-04-01T00:00:00+00:00","2017-05-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2017-05-01T00:00:00+00:00","2017-06-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2017-06-01T00:00:00+00:00","2017-07-01T00:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    bit_usd_stats_4hr = public_client.get_product_historic_rates('BTC-USD',"2017-07-01T00:00:00+00:00","2017-07-23T12:00:00+00:00",granularity=14400)
    num_4hr_candles = num_4hr_candles+len(bit_usd_stats_4hr)
    bit_usd_stats_4hr=sorted(bit_usd_stats_4hr,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats_4hr)):
        file.write(str(bit_usd_stats_4hr[x])+"\n")
        fourhr_unix_times.append(bit_usd_stats_4hr[x][0])
    bit_usd_stats_4hr.reverse()
    fourhr_data.append(bit_usd_stats_4hr)
    
    file.close()
    
    
    #write unix 4hr periods to file
    f1 = open("4hr_unix_times.txt","w")
    for x in range(len(fourhr_unix_times)):
        if x==(len(fourhr_unix_times)-1):
            f1.write(str(fourhr_unix_times[x]))
        else:
            f1.write(str(fourhr_unix_times[x])+"\n")
    
    f1.close()
    
    
    
    
    
    ###collect daily data and store in text file###
    
    global num_daily_candles
    global day_unix_times

    file = open("daily_candle_gdax_data.txt","w")
    bit_usd_stats1 = public_client.get_product_historic_rates('BTC-USD',"2015-01-01T00:00:00+00:00","2015-05-04T00:00:00+00:00",granularity=86400)
    num_daily_candles = num_daily_candles + len(bit_usd_stats1)
    bit_usd_stats1=sorted(bit_usd_stats1,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats1)):
        file.write(str(bit_usd_stats1[x])+"\n")
        day_unix_times.append(bit_usd_stats1[x][0])
    bit_usd_stats1.reverse()
    daily_data.append(bit_usd_stats1)
    
    
    bit_usd_stats2 = public_client.get_product_historic_rates('BTC-USD',"2015-05-04T00:00:00+00:00","2015-11-20T00:00:00+00:00",granularity=86400)
    num_daily_candles = num_daily_candles + len(bit_usd_stats2)
    bit_usd_stats2=sorted(bit_usd_stats2,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats2)):
        file.write(str(bit_usd_stats2[x])+"\n") 
        day_unix_times.append(bit_usd_stats2[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats2)) 
    #print(bit_usd_stats2)
    bit_usd_stats2.reverse()
    #print(bit_usd_stats2)
    daily_data.append(bit_usd_stats2)
    
    
    bit_usd_stats3 = public_client.get_product_historic_rates('BTC-USD',"2015-11-20T00:00:00+00:00","2016-06-07T00:00:00+00:00",granularity=86400)
    num_daily_candles = num_daily_candles + len(bit_usd_stats3)
    bit_usd_stats3=sorted(bit_usd_stats3,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats3)):
        file.write(str(bit_usd_stats3[x])+"\n") 
        day_unix_times.append(bit_usd_stats3[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats3))
    #print(bit_usd_stats3)
    bit_usd_stats3.reverse()
    #print(bit_usd_stats3)
    daily_data.append(bit_usd_stats3)

    
    bit_usd_stats4 = public_client.get_product_historic_rates('BTC-USD',"2016-06-07T00:00:00+00:00","2016-12-24T00:00:00+00:00",granularity=86400)
    num_daily_candles = num_daily_candles + len(bit_usd_stats4)
    bit_usd_stats4=sorted(bit_usd_stats4,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats4)):
        file.write(str(bit_usd_stats4[x])+"\n")  
        day_unix_times.append(bit_usd_stats4[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats4)) 
    #print(bit_usd_stats4)
    bit_usd_stats4.reverse()
    #print(bit_usd_stats4)
    daily_data.append(bit_usd_stats4)
    
    
    bit_usd_stats5 = public_client.get_product_historic_rates('BTC-USD',"2016-12-24T00:00:00+00:00","2017-07-12T00:00:00+00:00",granularity=86400)
    num_daily_candles = num_daily_candles + len(bit_usd_stats5)
    bit_usd_stats5=sorted(bit_usd_stats5,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats5)):
        file.write(str(bit_usd_stats5[x])+"\n")
        day_unix_times.append(bit_usd_stats5[x][0])
    #print("number of days/data pts: ", len(bit_usd_stats5)) 
    bit_usd_stats5.reverse()
    daily_data.append(bit_usd_stats5)

    
    #add daily data to the overall list to still account for passing days
    
    bit_usd_stats = public_client.get_product_historic_rates('BTC-USD',"2017-07-12T00:00:00+00:00","2017-07-23T00:00:00+00:00",granularity=86400) #go from date range of [last date entered]-[current date]
    bit_usd_stats=sorted(bit_usd_stats,key=lambda x: (x[0]))
    for x in range(len(bit_usd_stats)):
        if x==(len(bit_usd_stats)-1):
            file.write(str(bit_usd_stats[x]))
        else:
            file.write(str(bit_usd_stats[x])+"\n")
        day_unix_times.append(bit_usd_stats[x][0])
    bit_usd_stats.reverse()
    daily_data.append(bit_usd_stats)
    file.close()
    
    #write unix days to file
    f1 = open("day_unix_times.txt","w")
    for x in range(len(day_unix_times)):
        if x==(len(day_unix_times)-1):
            f1.write(str(day_unix_times[x]))
        else:
            f1.write(str(day_unix_times[x])+"\n")
    f1.close()
    
    
    return daily_data,fourhr_data


get_gdax_historical_data()
