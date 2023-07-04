#IMPORTS

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

#DATA HANDLING

path="FuelConsumptionCo2.csv"
df = pd.read_csv(path)

# print(df.head())

# This is the code that we use to show all the data in the cvs file

# print(df.describe())

# This is the code that we use to show data like the mean, count, max, min...

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
# print(cdf.head(9))

# This code will show you the data in the categories: Engine Size, Cylinders, Fuel Consumption Combined and
# Co2 Emissions, and futher more, it will only show the 9 first rows!

viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
# viz.hist()
# plt.show() Show the graph
# Here, we make the viz histogram with the categories above, the we display it.

# LINEAR PLOTTING Optional

# # plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color = "blue")
# # plt.xlabel("Fuel Consumption Combined") # Labeling the X axis
# # plt.ylabel("Co2 Emissions") # Labeling the Y axis
# # plt.title("Fuel Consumption Combined vs Co2 Emissions") # Title of the graph
# # plt.show()
# # 
# # plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='red')
# # plt.xlabel("Engine size")
# # plt.ylabel("Co2 Emissions")
# # plt.title("Engine size vs Co2 Emissions")
# # plt.show()

# Here, we made the scatter plots for Engine size and Fuel Consumption Combined and then we display it.

# Practise: Plot CYLINDERS vs the Emission, to see how linear is their relationship is:

# Answer:

# # plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='green')
# # plt.xlabel("Cylinders")
# # plt.ylabel("Co2 Emissions")
# # plt.title("Cylinders vs Co2 Emissions")
# # plt.show()

# TRAINING THE COMPUTER (for Engine Size)

# Answer: It's not really linear

splitcases = np.random.rand(len(df)) < 0.8  # np.random.rand() makes a mask so that we can select truly random rows in the data set
train = cdf[splitcases]
test = cdf[~splitcases]

# Here we split 80% of all of the data into train and 20% of the data into test cases.

from sklearn import linear_model
regr = linear_model.LinearRegression() # We indentify which type of Computer Learning algorithm it is (Linear Regression)
train_x = np.asanyarray(train[['ENGINESIZE']]) # Right here, we train the x axis
train_y = np.asanyarray(train[['CO2EMISSIONS']]) # Right here, we train the y axis
regr.fit(train_x, train_y) # Right here the skit-learn library finds the fit line for us
# The coefficients
# print ('Coefficients: ', regr.coef_) # The slope
# print ('Intercept: ',regr.intercept_) # The y Intercept

# This is maybe one of the hardest parts of the code, this is where we find the fit line in the data using the y = mx+b
# equation where m is the slope and where b is the intercept.

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], 'black', label = "Fit Line")
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.legend(loc="upper left")
plt.title("Engine size vs Co2 Emissions")

plt.show()

# Oof this is the hardes part of this code, in line 79 we use the y= mx+b equation with regr.coef being our slope and
# regr.intercept being our y intercept.

# TESTING IT AND THEN RATING THE TESTING

from sklearn.metrics import r2_score

test_x = np.asanyarray(test[['ENGINESIZE']]) # Testing the x axis
test_y = np.asanyarray(test[['CO2EMISSIONS']]) # Testing the y axis
test_y_ = regr.predict(test_x) # Using the graph to predict an unknown value of CO2EMISSIONS using ENGINESIZE as reference

# print(test_y_) # The CO2EMISSIONS of the test cases

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y))) # Just average error
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2)) # The mean of the squared errors (Note: to research more about it)
print("Rsquared-score: %.2f" % r2_score(test_y , test_y_) ) # How close is your data to fitting your line. 1 is the highest and 0 is the lowest.

# EXERCISE: Do a train and test with the measurement of FUELCONSUMPTION_COMB

regr = linear_model.LinearRegression()
train_x1 = np.asanyarray(train[['FUELCONSUMPTION_COMB']])
train_y1 = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x1, train_y1)

plt.scatter(train.FUELCONSUMPTION_COMB, train.CO2EMISSIONS,  color='red')
plt.plot(train_x1, regr.coef_[0][0]*train_x1 + regr.intercept_[0], 'black', label = "Fit line")
plt.xlabel("Fuel Consumption Combined")
plt.ylabel("Co2 Emissions")
plt.legend(loc="upper left")
plt.title("Fuel COnsumption Combined vs Co2 Emissions")

plt.show()

test_x1 = np.asanyarray(test[['ENGINESIZE']])
test_y1 = np.asanyarray(test[['CO2EMISSIONS']])
test_y_1 = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_1 - test_y1)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_1 - test_y1) ** 2))
print("Rsquared-score: %.2f" % r2_score(test_y1 , test_y_1) )

# Answer: We can see that using the Engine Sized resulted in a farther off answer because it isn't very linear.