# Solving Driver Telematics Analysis using Neural Networks
 
##Problem Statement

We are given about 200 routes taken by each of the 1711 drivers. Each route is represented as a sequence of ```x,y``` coordinates that represent measurements of a driver's GPS location sampled every second. Coordinates start at point ```0,0``` and are in meters so a driver that is first at ```2,3``` and then moves to  ```3,3``` has moved a total of 3 meters. [Download data here](https://www.kaggle.com/c/axa-driver-telematics-analysis/data)

Given a new trip, the task is to identify trips which are not from the driver of interest based on their telematic features. The expected output is the predicted probability of the trip belonging to the driver of interest.

##Setting up the tools

I started with a free version of EC2 and setup the required dependencies for Theano, Keras and IPython. Since I unfortunately don't own a GPU at home, I instead prepared code to run on an AWS GPU. I also prepared some scripts to detect free AWS instances and given more time would like to distribute different network configurations on different processes and different AWS instances.

```
sh setup.sh
```

Then to make sure that Theano libraries were properly imported and that it can detect the GPU I ran the two below scripts.

```
python configuration-testing/working.py

python configuration-testing/gpu-check.py
```

##Idea 1: Convolutional Neural Nets: encoding trips as images

*Proposed solution in solution folder*

A trip is given to us as a sequence of  ```x,y``` pair of coordinates this describes a path in a 2D plane. It is therefore possible to turn our text data into image data and feed it into a convolutional neural network and have the last layer contain one node for each driver to make a classification.

We do the transformation using the networkx library

![Networkx path](images/networkxpath.png)

Alternatively we could have just done a simple line plot on the plane but this encoding should keep the same amount of information since darker colors correspond to jittier movements

The convolutional neural network is fairly standard and the keras code is highly readable. For example: ```model.add(Dropout(0.25))``` means 25% of the nodes in a layer will be dropped to improve generalization capabilities and ```model.add(Dense(128,nb_classes))``` is read as a layer with ```128``` inputs and ```nb_classes``` output nodes. The network works by feeding in one route encoded as a ```28x28``` pixel image at a time with a known driver label. Experiment was done on ```10``` drivers each with 200 routes and the goal is to predict from the test set the driver identity from the route and that's what the last softmax layer is doing. I then separate out 20% of the data for testing purposes and train the neural net on the remaining 80% and report the accuracy of the net.

```python
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


```


##Next steps:

There were many ideas I wanted to explore but did not have the time to since I worked on this seriously mainly on Saturday June 13 to think of different approaches to solve the problem and read some relevant literature and Saturday June 20 to wire everything up together.

* Obviously my code is incredibly messy, logic is duplicated many times in the same file. The directory substructure follows my chronology through trying to solve this problem as opposed to a logical separation of helper scripts, core source scripts and data
* To make it easier to check the performance of candidate neural net architectures, I setup in up the ```Flask``` folder some code that just pipes all of ```stdout``` and ```stderr``` to a browser. That way after I run some architecture, I can check in on it really quickly from my phone or otherwise to see if anything interesting is going on.
* Working with Python was painfully slow, if I could do this again I would do it using Lua and Torch instead
* Get a better computer with two GPU's, an IDE like Komodo is very useful since I constantly need to know the values and types of all my variables to debug problems but my measly macbook air was not cutting it. Mounting my EC2 instance file system locally was also painfully slow. Creating the images locally was painfully slow so I tried to have a different process run for each driver simultaneously but my Python was hogging my machine and made it unusable
* Keras code runs on GPU automatically if it can, I also have some scripts to check if Theano can properly communicate with the GPU but I did not have time to run enough experiments to study the speedup
* It's tricky to tell beforehand which architectures will work well so it'll be useful to have a config file that would be loaded by a main script and then create a keras neural net with the specified configuration and run it on a GPU on AWS
* Feed in each route as a sequence of ```x,y``` coordinate to a recurrent neural network with a multinomial logistic regression at the output layer. Sample Code in ```Keras-nets/recurrent-net.py```
* PIL has an antialias mode to maintain a good image quality after an image is compressed, unfortunately it doesn't necessarily resize the image with given width and height parameters. it even silently ignores them and finds a good approximation to the given size. Next time I'll write my own helper scripts to make sure this doesn't happen
