#!/usr/bin/python


"""
Take folder containing a folder of drivers and for each driver route turn
it into a network and plot it, resize it and save it

"""

import numpy
import networkx as nx
import matplotlib.pyplot as plt
import os
import sys
import Image
import pdb

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
    plt.show()

    print "displaying graph" + file_name
    pdb.set_trace()
    image_name = file_name.replace("csv", "png")
    plt.savefig(image_name,bbox_inches='tight')
    print "saved graph"


    return image_name

def coord_to_line_plot(file_name):
    with open(file_name) as f:
        print "Reading driver on route %s" %(file_name)
        next(f)
        coord_list = [line.split(",") for line in f]

    plt.figure()
    plt.plot(*zip(*coord_list))
    plt.show()




def resize_image_save(width=25,height=25,infile=""):
    """
    Given a list of image names, resize them to width x height in pixels
    ANTIALIAS to preserve quality of the image
    Save compressed image in the same directory as the larger image
    """
    size = width,height

    try:
        pdb.set_trace()
        print "resize_image_save---infile: " + infile
        im = Image.open(infile)
        im.thumbnail(size,Image.ANTIALIAS)
        resized_image_name = infile.replace(".png", "_small.png")
        im.save(resized_image_name,"png")
        return resized_image_name

    except IOError:
        print "cannot create thumbnail for '%s'" % infile


def next_file():
    """
    Idea for refactoring, does not honestly save that much typing
    """
    for driver in os.listdir("drivers"):
        for route_number in os.listdir(driver):
            file_name = "drivers/" + driver + route_number
            yield file_name


def find_largest_x_y():
    """
    Find largest x coordinate and largest y coordinate,
    Returned values need not be associated to the same point

    This will become obsolete after I implement the flatten operation
    since I'll only need to do a linear scan
    """
    x_max = 0.0
    y_max = 0.0
    for driver in os.listdir("drivers"):
        for route_number in os.listdir(driver):
            file_name = "drivers/" + driver + route_number
            with open(file_name) as f:
                next(f)
                for line in f:
                    x,y = line.split(",")
                    x = max(abs(x), abs(x_max))
                    y = max(abs(y), abs(y_max))

    print "the maximal values are" %(x,y)
    return x,y


if __name__ == "__main__":
    file_name  = "../1/1.csv"
    image_name = coord_to_graph_image(file_name)
    # print "created larger image: " + image_name
    # resized_image_name = resize_image_save(infile = image_name)
    # print "converted to smaller image: " + resized_image_name
    #print all images for driver 1
     # for file_name in os.listdir("../1"):
     #     print file_name
     #     coord_to_graph_image("1/" + file_name)
     #     coord_to_line_plot("../1/" + file_name)
    #find_largest_x_y()



    """
    for driver in os.listdir("drivers"):
        for route_number in os.listdir(driver):
            coord_to_graph_image("drivers/" + driver + route_number)
    """
