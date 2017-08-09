import numpy as np
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler


'''
Create the time series data from original data
'''

#Create the lagged sliding window of 1 to house time series data
prices = []
ask = []
bid = []
temp_p = []
temp_a = []
temp_b = []

file = open("OrderBookData.txt", "r")
for line in file:
    line = line.strip("\n") #strips \n from end of each line
    j=0 #counter for each array placement
    for word in line.split(","): #splits line into individual items by ","
        if j==1: #price
            temp_p.append(float(word))
        elif j==2: #ask volume
            temp_a.append(float(word))
        elif j==3: #big volume
            temp_b.append(float(word))
        j=j+1

        
del temp_p[0] #removes first price since they'll be shifted down
del temp_a[-1] #removes last ask volume since prices will be shifted down there'll be no corresponding future price to map to
del temp_b[-1] #removes last ask volume since prices will be shifted down there'll be no corresponding future price to map to
prices = temp_p
ask = temp_a
bid = temp_b

'''
print("prices: ",prices[:3],prices[-3:])
print("ask: ",ask[:3],ask[-3:])
print("bid",bid[:3],bid[-3:])
'''

#Combine time series data into a 2d numpy array to use to train model
data = np.empty(shape=(len(prices),2), dtype = np.float) 
price = np.empty(shape=(len(prices),), dtype = np.float) 

for i in range(len(prices)):
    for j in range(3):
        if j==0: #price
            price[i] = prices[i]
        elif j==1: #ask volume
            data[i][j-1] = ask[i]
        elif j==2: #big volume
            data[i][j-1] = bid[i]
        else:
            print("Error!")

    
#print("Data! ", data[:2], data[-2:])

'''
Data Arrangement Completed
'''

#Configure and test algorithm
