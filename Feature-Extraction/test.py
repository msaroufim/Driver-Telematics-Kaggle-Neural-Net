#!/usr/bin/env python

"""
Take folder containing a folder of drivers and for each driver route turn
it into a network and plot it, resize it and save it

"""

import numpy
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

def next_file():
    """
    Idea for refactoring, does not honestly save that much typing
    """
    for driver in os.listdir("drivers"):
        for route_number in os.listdir(driver):
            file_name = "drivers/" + driver + route_number
            yield file_name




def main(driver):
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
        resized_image_name = resize_image_save( coord_to_graph_image(path + '/' + route_number) ,25,25)
        dataset.append([resized_image_name,driver])
        #random.shuffle(dataset) will shuffle it properly in place so no return value
    print '-'*50
    print dataset
    return dataset


if __name__ == "__main__":
    #NUM_DRIVERS = 10
    for i in [1,10,100,1000,1001]:
        p = multiprocessing.Process(target=main,args=(i,))
        p.start()
