#!/usr/bin/env python

"""
Take folder containing a folder of drivers and for each driver route turn
it into a network and plot it, resize it and save it

"""

import networkx as nx
import matplotlib.pyplot as plt
import os
import sys
from PIL import Image
import pdb
import random
import multiprocessing

def coord_to_graph_image(file_name):


    G = nx.Graph()
    with open(file_name) as f:
        print "Reading driver_name on route %s" %(file_name)
        next(f)
        for i, line in enumerate(f):
            x,y = line.split(",")
            print x,y
            G.add_node(i,pos=(x,y))

    pos = nx.get_node_attributes(G,'pos')
    print "constructed graph for " + file_name

    plt.figure()
    nx.draw(G,pos)
    #plt.show()

    print "displaying graph" + file_name
    #pdb.set_trace()
    image_name = file_name.replace("csv", "png")
    plt.savefig(image_name,bbox_inches='tight')
    print "saved graph"
    print "image name:" + image_name
    return image_name






def resize_image_save(infile,width,height):
    """
    Given a list of image names, resize them to width x height in pixels
    ANTIALIAS to preserve quality of the image
    Save compressed image in the same directory as the larger image
    """
    size = width,height

    #pdb.set_trace()
    print "resize_image_save---infile: " + infile
    im = Image.open(infile)
    im.thumbnail(size,Image.ANTIALIAS)
    resized_image_name = infile.replace("drivers","thumbnail"+str(height))
    #resized_image_name = infile.replace(".png", "_small.png")

    if not os.path.exists(os.path.dirname(resized_image_name)):
        os.makedirs(os.path.dirname(resized_image_name))


    im.save(resized_image_name,"png")

    return resized_image_name



def preprocess(driver):
    dataset = []
    data_location = "./drivers/"
    #for driver in os.listdir(data_location):
    path = data_location + str(driver)
    for route_number in os.listdir(path):

        route_filename = path + '/' + route_number
        if route_filename.endswith(".png"):
            continue
        #image_name = coord_to_graph_image(route_filename)
        #print "Image name is: " + image_name


        #CHANGE IF NEEDED TO DIFFERENT SIZE, TRY TO KEEP IT SQUARE
        resized_image_name = resize_image_save( coord_to_graph_image(path + '/' + route_number) ,28,28)

        resized_image = Image.open(resized_image_name)
        image_numpy = np.asarray(resized_image)

        dataset.append([image_numpy,driver])

    #random.shuffle(dataset) shuffles dataset in place
    random.shuffle(dataset)
    (X_train, y_train) = dataset[0:int(len(dataset)*0.8)][0], dataset[0:int(len(dataset)*0.8)][1]
    (X_test, y_test) = dataset[int(len(dataset)*0.8 + 1):int(len(dataset))][0],dataset[int(len(dataset)*0.8 + 1):len(dataset)][1]
    print '-'*50
    return dataset



#NUM_DRIVERS = 3612
for i in [1,10,11,12,13,14,15,16,2,3]:
    p = multiprocessing.Process(target=preprocess,args=(i,))
    p.start()


from __future__ import absolute_import
from __future__ import print_function
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import numpy as np

'''
    Train a simple convnet
    Run on GPU: THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python mnist_cnn.py
    Get to 99.25% test accuracy after 12 epochs (there is still a lot of margin for parameter tuning).
    16 seconds per epoch on a GRID K520 GPU.
'''

batch_size = 10
nb_classes = 10
nb_epoch = 15

# the data, shuffled and split between tran and test sets
#(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")
X_train /= 255
X_test /= 255
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

model.add(Convolution2D(32, 1, 3, 3, border_mode='full'))
model.add(Activation('relu'))
model.add(Convolution2D(32, 32, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(poolsize=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(32*196, 128))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(128, nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adadelta')

model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch, show_accuracy=True, verbose=2, validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, show_accuracy=True, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])


