# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 12:09:43 2018

@author: amar.nag9@gmail.com
"""
from keras.models import Sequential
from keras.models import Model
from keras.layers import Input, Conv2D
from keras.optimizers import Adam

def srcnn(input_shape=(33,33,1)):
    model = Sequential()
    model.add(Conv2D(64, (9, 9), input_shape=input_shape, activation='relu', padding="valid"))
    model.add(Conv2D(32, (1, 1), activation='relu', padding="valid"))
    model.add(Conv2D(1, (5, 5), ))
    model.compile(Adam(lr=0.00003), 'mse')
    return model