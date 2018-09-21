# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:56:34 2018

@author: amar.nag9@gmail.com
"""

import os
import h5py
import network
import argparse
from keras.callbacks import TensorBoard
import time
tic=time.time()

def train():

    model = network.srcnn()

    output_file = './data.h5'
    h5f = h5py.File(output_file, 'r')
    X = h5f['input']
    y = h5f['label']

    n_epoch = args.n_epoch

    if not os.path.exists(args.save):
        os.mkdir(args.save)

    for epoch in range(0, n_epoch, 5):
        tensor_board = TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)
        model.fit(X, y, batch_size=128, nb_epoch=5, shuffle='batch',validation_split=0.2,callbacks=[tensor_board])
        if args.save:
            print("Saving model ", epoch + 5)
            model.save(os.path.join(args.save, 'model_%d.h5' %(epoch+5)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', '--save',
                        default='./save',
                        dest='save',
                        type=str,
                        nargs=1,
                        help="Path to save the checkpoints to")
    parser.add_argument('-E', '--epoch',
                        default=10,
                        dest='n_epoch',
                        type=int,
                        nargs=1,
                        help="Training epochs must be a multiple of 5")
    args = parser.parse_args()
    print(args)
    train()
    toc=time.time()
    duration=(toc-tic)/3600
    print(duration)