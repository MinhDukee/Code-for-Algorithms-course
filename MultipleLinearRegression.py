#IMPORTS

import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#DATA HANDLING

path="FuelConsumption.csv"
df = pd.read_csv(path)

# print(df.head())

# This is the code that we use to show all the data in the cvs file

# print(df.describe())

# This is the code that we use to show data like the mean, count, max, min...

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

# print(cdf.head(9))

# This code will show you the data in the categories: Engine Size, Cylinders, Fuel Consumption Combined, Fuel Consumption City, Fuel Consumption HWY
# and Co2 Emissions, and futher more, it will only show the 9 first rows!

#SPLITTING THE DATA

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

from sklearn import linear_model
regr = linear_model.LinearRegression()
x = np.asanyarray(train[['ENGINESIZE','CYLINDERS']])
y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(x, y)
# The coefficients
print ('Coefficients: ', regr.coef_)

y_hat= regr.predict(test[['ENGINESIZE','CYLINDERS']])
x = np.asanyarray(test[['ENGINESIZE','CYLINDERS']])
y = np.asanyarray(test[['CO2EMISSIONS']])
print("Residual sum of squares: %.2f"
      % np.mean((y_hat - y) ** 2))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(x, y))
# PLOTTING
plt.style.use('default')

fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
    ax.plot(train.ENGINESIZE, train.CO2EMISSIONS, train.CYLINDERS, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
    ax.set_xlabel('Engine Size', fontsize=12)
    ax.set_ylabel('Cylinders', fontsize=12)
    ax.set_zlabel('CO2 Emissions', fontsize=12)
    ax.locator_params(nbins=4, axis='x')
    ax.locator_params(nbins=5, axis='x')



ax1.view_init(elev=28, azim=120)
ax2.view_init(elev=4, azim=114)
ax3.view_init(elev=60, azim=165)

fig.tight_layout()
fig.show()