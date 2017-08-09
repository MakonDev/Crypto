from bayesian_regression import *
import time

start = time.time() #start timer

# Retrieve price, v_ask, and v_bid data points from the text file.
prices = []
v_ask = []
v_bid = []
num_points = 0 #counter for number of data points in data set

file = open("OrderBookData.txt", "r")
for line in file:
    num_points+=1
    line = line.strip("\n") #strips \n from end of each line
    j=0 #counter for each array placement
    for word in line.split(","): #splits line into individual items by ","
        #print(word)
        if j==1: #price
            prices.append(float(word))
        elif j==2: #ask volume
            v_ask.append(float(word))
        elif j==3: #big volume
            v_bid.append(float(word))
        j=j+1
        
file.close()

'''
print("Number of data points: ",num_points)
print(prices[:3],prices[(num_points-3):(num_points)])
print(v_ask[:3],v_ask[(num_points-3):(num_points)])
print(v_bid[:3],v_bid[(num_points-3):(num_points)])
'''


# Divide prices into three, roughly equal sized, periods:
# prices1, prices2, and prices3.
[prices1, prices2, prices3] = np.array_split(prices, 3)

# Divide v_bid into three, roughly equal sized, periods:
# v_bid1, v_bid2, and v_bid3.
[v_bid1, v_bid2, v_bid3] = np.array_split(v_bid, 3)

# Divide v_ask into three, roughly equal sized, periods:
# v_ask1, v_ask2, and v_ask3.
[v_ask1, v_ask2, v_ask3] = np.array_split(v_ask, 3)

# Use the first time period (prices1) to generate all possible time series of
# appropriate length (180, 360, and 720).
timeseries180 = generate_timeseries(prices1, 180)
timeseries360 = generate_timeseries(prices1, 360)
timeseries720 = generate_timeseries(prices1, 720)

'''
print(all(isinstance(x, float) for x in timeseries180))
print(all(isinstance(x, float) for x in timeseries360))
print(all(isinstance(x, float) for x in timeseries720))
'''

# Cluster timeseries180 in 100 clusters using k-means, return the cluster
# centers (centers180), and choose the 20 most effective centers (s1).
centers180 = find_cluster_centers(timeseries180, 100)
s1 = choose_effective_centers(centers180, 20)

centers360 = find_cluster_centers(timeseries360, 100)
s2 = choose_effective_centers(centers360, 20)

centers720 = find_cluster_centers(timeseries720, 100)
s3 = choose_effective_centers(centers720, 20)

# Use the second time period to generate the independent and dependent
# variables in the linear regression model:
# Δp = w0 + w1 * Δp1 + w2 * Δp2 + w3 * Δp3 + w4 * r.
Dpi_r, Dp = linear_regression_vars(prices2, v_bid2, v_ask2, s1, s2, s3)

# Find the parameter values w (w0, w1, w2, w3, w4).
w = find_parameters_w(Dpi_r, Dp)

# Predict average price changes over the third time period.
dps = predict_dps(prices3, v_bid3, v_ask3, s1, s2, s3, w)

# What's your 'Fuck You Money' number?
bank_balance = evaluate_performance(prices3, dps, t=0.01, step=1)

print(bank_balance)

end = time.time()
print("Duration: " + str(end - start) +" seconds, or " +str((end - start)/60)+" minutes")