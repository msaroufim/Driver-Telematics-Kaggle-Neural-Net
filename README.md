# Solving Driver Telematics Analysis using Neural Networks
 
##Problem Statement

We are given about 200 routes taken by each of the 1711 drivers. Each route is represented as a sequence of ```x,y``` coordinates that represent measurements of a driver's GPS location sampled every second. Coordinates start at point ```0,0``` and are in meters so a driver that is first at ```2,3``` and then moves to  ```3,3``` has moved a total of 3 meters. [Download data here](https://www.kaggle.com/c/axa-driver-telematics-analysis/data)

Given a new trip, the task is to identify trips which are not from the driver of interest based on their telematic features. The expected output is the predicted probability of the trip belonging to the driver of interest.

##Setting up the tools

I started with a free version of EC2 and setup the required dependencies for Theano, Pylearn2 and IPython. Since I unfortunately don't own a GPU at home, I instead expect to take advantage of AWS for this as well.

```
sh setup.sh
```

Then to make sure that Theano libraries were properly imported and that it can detect the GPU I ran the two below scripts.

```
python configuration-testing/working.py

python configuration-testing/gpu-check.py
```

##Idea 1: Convolutional Neural Nets: encoding trips as images

A trip is given to us as a sequence of  ```x,y``` pair of coordinates this describes a path in a 2D plane. It is therefore possible to turn our text data into image data and feed it into a convolutional neural network with a multinomial linear regeressor at the output layer. 

We do the transformation using the networkx library

![Networkx path](images/networkxpath.png)

Alternatively we could have just done a simple line plot on the plane but this encoding should keep the same amount of information since darker colors correspond to jittier movements.

TODO: need to think some more about what's a good size for these images and what's a good thickness and scale for the paths. Idea is to scale all images based on longest path in the dataset.


##Idea 2: Recurrent Neural Networks sequence learning

Feed in each ```x,y``` coordinate to a recurrent neural network with a multinomial logistic regression at the output layer to predict the most likely driver and use a function of that difference as the error to backpropagate.
