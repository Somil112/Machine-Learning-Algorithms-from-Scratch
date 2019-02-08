# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:30:24 2019

@author: Somil
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,[0]].values
Y = dataset.iloc[:,[1]].values




mean_X = np.sum(X)/len(X)
mean_Y = np.sum(Y)/len(Y)

b1_numerator = np.sum((X-mean_X)*(Y-mean_Y))
b1_denom = np.sum(np.square(X-mean_X))

b1 = b1_numerator/b1_denom

b0 = mean_Y - b1*mean_X

y_pred = b0 + b1*X

plt.scatter(X,Y,c='red')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.plot(X,y_pred)
plt.show()


regressor = LinearRegression()
regressor.fit(X,Y)

regressor.predict(X)




#Seems Linear, so we use Linear Regression


