# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:28:59 2019

@author: Somil
"""

import pandas as pd
import numpy as np
from collections import Counter

dataset = pd.read_csv('nb.csv')

class_count = dict(Counter(dataset["Class"]))

p_go_out = class_count['go-out']/float(len(dataset))
p_stay_home = class_count['stay-home']/float(len(dataset))

p_sunny_go_out = 0.0
p_sunny_stay_home = 0.0
p_rainy_go_out = 0.0
p_rainy_stay_home = 0.0
p_working_go_out = 0.0
p_working_stay_home = 0.0 
p_broken_go_out = 0.0
p_broken_stay_home = 0.0



for i in range(len(dataset)):
    if dataset["Weather"][i] == 'sunny' and dataset["Class"][i] == 'go-out':
        p_sunny_go_out += 1
    if dataset["Weather"][i] == 'sunny' and dataset["Class"][i] == 'stay-home':
        p_sunny_stay_home += 1
    if dataset["Weather"][i] == 'rainy' and dataset["Class"][i] == 'go-out':
        p_rainy_go_out += 1
    if dataset["Weather"][i] == 'rainy' and dataset["Class"][i] == 'stay-home':
        p_rainy_stay_home += 1
    if dataset["Car"][i] == 'working' and dataset['Class'][i] == 'go-out':
        p_working_go_out +=1
    if dataset["Car"][i] == 'working' and dataset['Class'][i] == 'stay-home':
        p_working_stay_home +=1
    if dataset["Car"][i] == 'broken' and dataset['Class'][i] == 'go-out':
        p_broken_go_out +=1
    if dataset["Car"][i] == 'broke' and dataset['Class'][i] == 'stay-home':
        p_broken_stay_home +=1
    
p_sunny_go_out = p_sunny_go_out/class_count['go-out']
p_rainy_go_out = p_rainy_go_out/class_count['go-out']
p_working_go_out = p_working_go_out/class_count['go-out']
p_broken_go_out = p_broken_go_out/class_count['go-out']

p_sunny_stay_home = p_sunny_stay_home/class_count['stay-home']
p_rainy_stay_home = p_rainy_stay_home/class_count['stay-home']
p_working_stay_home = p_working_stay_home/class_count['stay-home']
p_broken_stay_home = p_broken_stay_home/class_count['stay-home']
    
p_sunny_working_go_out = p_sunny_go_out*p_working_go_out*p_go_out
p_sunny_working_stay_home = p_sunny_stay_home*p_working_stay_home*p_stay_home

p_sunny_broken_go_out = p_sunny_go_out*p_broken_go_out*p_go_out
p_sunny_broken_stay_home = p_sunny_stay_home * p_broken_stay_home * p_stay_home
 
p_rainy_working_go_out = p_rainy_go_out * p_working_go_out * p_go_out
p_rainy_working_stay_home = p_rainy_stay_home * p_working_stay_home *p_stay_home

p_rainy_broken_go_out = p_rainy_go_out *p_broken_go_out *p_go_out
p_rainy_broken_stay_home = p_rainy_stay_home * p_broken_stay_home * p_stay_home

dataset['go-out']  = 0.0
dataset['stay-home'] = 0.0


for i in range(len(dataset)):
    if(dataset['Weather'][i] == 'sunny' and dataset['Car'][i] == 'working'):
        dataset.at[i,'go-out'] = p_sunny_working_go_out
        dataset.at[i,'stay-home'] = p_sunny_working_stay_home
    if(dataset['Weather'][i] == 'sunny' and dataset['Car'][i] == 'broken'):
        dataset.at[i,'go-out'] = p_sunny_broken_go_out
        dataset.at[i,'stay-home'] = p_sunny_broken_stay_home
    if(dataset['Weather'][i] == 'rainy' and dataset['Car'][i] == 'working'):
        dataset.at[i,'go-out'] = p_rainy_working_go_out
        dataset.at[i,'stay-home'] = p_rainy_working_stay_home
    if(dataset['Weather'][i] == 'rainy' and dataset['Car'][i] == 'broken'):
       dataset.at[i,'go-out'] = p_rainy_broken_go_out
       dataset.at[i,'stay-home'] = p_rainy_broken_stay_home
       
print("Final Results")
print(dataset)

from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing

X = dataset.iloc[:,[0,1]].values
y = dataset.iloc[:,[2]].values

labelencoder_x1 = preprocessing.LabelEncoder()

labelencoder_x1.fit(X[:,[0]])
X[:,[0]] = labelencoder_x1.transform(X[:,[0]]).reshape(10,1)

labelencoder_x2 = preprocessing.LabelEncoder()

labelencoder_x2.fit(X[:,[1]])
X[:,[1]] = labelencoder_x2.transform(X[:,[1]]).reshape(10,1)

labelencoder_y = preprocessing.LabelEncoder()

labelencoder_y.fit(y)
y = labelencoder_y.transform(y).reshape(10,1)




gnb = GaussianNB()
y_pred = gnb.fit(X,y).predict(X)

y_pred = labelencoder_y.inverse_transform(y_pred)