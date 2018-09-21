# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:33:04 2018

@author: amar.nag9@gmail.com
"""

from keras.models import Sequential
from keras.layers import Conv2D
from keras.optimizers import Adam
import numpy as np
import time
import imageio

# Scale factor s=3
scale=3
tic= time.time()

# Model used for Training and Testing
def predict_model():
 SRCNN = Sequential()
 SRCNN.add(Conv2D(64, (9, 9), input_shape=(None, None, 1), activation="relu", padding="valid"))
 SRCNN.add(Conv2D(32, (1, 1), activation="relu", padding="valid"))
 SRCNN.add(Conv2D(1, (5, 5), ))
 SRCNN.compile(Adam(lr=0.00003), "mse")
 return SRCNN

# Generating the Testing image
srcnn_model = predict_model()
srcnn_model.load_weights("./save/model_1010.h5")
IMG_NAME = "./Testx3Lum/Set5/butterfly_GT.bmp"
OUTPUT_NAME="butterfly_SRCNN.bmp"
Y_img = imageio.imread(IMG_NAME)
Y = np.zeros((1, Y_img.shape[0], Y_img.shape[1], 1), dtype=float)
Y[0, :, :,0] = Y_img.astype(float) / 255
pre = srcnn_model.predict(Y) * 255.
pre[pre[:] > 255] = 255
pre[pre[:] < 0] = 0
pre = pre.astype(np.uint8)
Y_img[6: -6, 6: -6] = pre[ 0, :, :, 0]
imageio.imwrite(OUTPUT_NAME, Y_img)
toc=time.time()
duration =(toc-tic)*1000
print("time taken in ms:",duration)