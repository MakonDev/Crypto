import gdax
import schedule
import json
import requests
from datetime import datetime
from pytz import utc
from apscheduler.schedulers.blocking import BlockingScheduler


def write_data(date,price,ask_vol,bid_vol):
    string = str(date)+","+str(price)+","+str(ask_vol)+","+str(bid_vol)+"\n"
    print(string)
    file = open("OrderBookData.txt", "a")
    file.write(string)
    file.close()
    
    return "Appended"


def pull_depth():
    public_client = gdax.PublicClient() #creates public client object
    depth = public_client.get_product_order_book('BTC-USD', level=2)
    ticker = public_client.get_product_ticker('BTC-USD')
    price = float(ticker['price'])
    date = ticker['time']
    #Collect bid volume
    bid_vol = 0
    for bid in depth['bids']:
        bid_vol += float(bid[1])
    #Collect ask volume
    ask_vol = 0
    for ask in depth['asks']:
        ask_vol += float(ask[1])
    write_data(date,price,ask_vol,bid_vol)
    
    return depth

#pull_depth()



def main():
    """Run pull_depth() at the interval of every ten seconds."""
    scheduler = BlockingScheduler(timezone=utc)
    scheduler.add_job(pull_depth, 'interval', seconds=10)
    try:
        scheduler.start()
        print("Tick")
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()