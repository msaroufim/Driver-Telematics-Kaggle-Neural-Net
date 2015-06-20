import numpy as np
import pandas as pd

#Keras runs automatically on GPU if it is found
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils


# Creating the model which consists of 3 conv layers followed by
# 2 fully connected layers
print('creating the model')

# Sequential wrapper model
model = Sequential()

# first convolutional layer
model.add(Convolution2D(32,1,2,2))
model.add(Activation('relu'))

# second convolutional layer
model.add(Convolution2D(48, 32, 2, 2))
model.add(Activation('relu'))
model.add(MaxPooling2D(poolsize=(2,2)))

# third convolutional layer
model.add(Convolution2D(32, 48, 2, 2))
model.add(Activation('relu'))
model.add(MaxPooling2D(poolsize=(2,2)))

# Flatten to make inputs fit into fully connected layer
model.add(Flatten())

# first fully connected layer
model.add(Dense(32*6*6, 128, init='lecun_uniform'))
model.add(Activation('relu'))
model.add(Dropout(0.25))

# second fully connected layer
model.add(Dense(128, 128, init='lecun_uniform'))
model.add(Activation('relu'))
model.add(Dropout(0.25))

# last fully connected layer which output classes
model.add(Dense(128, 10, init='lecun_uniform'))
model.add(Activation('softmax'))

# setting sgd optimizer parameters
sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)

# categorical cross entropy H(p,q) = - \sum_x p(x) log(q(x)) between true distribution p and and learned distribution q
model.compile(loss='categorical_crossentropy', optimizer=sgd)



print('read data')
# reading training data

# split training labels and pre-process them
training_targets = training.ix[:,0].values.astype('int32')
training_targets = np_utils.to_categorical(training_targets)

# split training inputs
training_inputs = (training.ix[:,1:].values).astype('float32')

# read testing data
testing_inputs = (pd.read_csv('/home/mnist/test.csv').values).astype('float32')



# # pre-process training and testing data

# def de_mean():
#     max_value = np.max(training_inputs)
#     training_inputs /= max_value
#     testing_inputs /= max_value

#     mean_value = np.std(training_inputs)
#     training_inputs -= mean_value
#     testing_inputs -= mean_value

# de_mean()

# from scipy import misc
# arr = misc.imread(image_name)

# reshaping training and testing data so it can be fed to convolutional layers
training_inputs = training_inputs.reshape(training_inputs.shape[0], 1, 28, 28)
testing_inputs = testing_inputs.reshape(testing_inputs.shape[0], 1, 28, 28)


print("Starting training")
model.fit(training_inputs, training_targets, nb_epoch=10, batch_size=1000, validation_split=0.1, show_accuracy=True,shuffle=True,verbose=2)


print("Generating predictions")
preds = model.predict_classes(testing_inputs, verbose=0)

def write_preds(preds, fname):
    pd.DataFrame({"ImageId": list(range(1,len(preds)+1)), "Label": preds}).to_csv(fname, index=False, header=True)

print('Saving predictions')
write_preds(preds, "keras-mlp.csv")
