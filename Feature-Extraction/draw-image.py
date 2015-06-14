"""
Take folder containing a folder of drivers and for each driver route turn
it into a network and plot it

"""

import numpy
import networkx as nx
import matplotlib.pyplot as plt
import os

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
    plt.figure()
    nx.draw(G,pos)
    plt.show()
    print "Drew node"

def coord_to_line_plot(file_name):
    with open(file_name) as f:
        print "Reading driver on route %s" %(file_name)
        next(f)
        coord_list = [line.split(",") for line in f]

    plt.figure()
    plt.plot(*zip(*coord_list))
    plt.show()

if __name__ == "__main__":
    #print all images for driver 1
    for file_name in os.listdir("../1"):
        print file_name
        #coord_to_graph_image("1/" + file_name)
        coord_to_line_plot("../1/" + file_name)


    """
    for driver in os.listdir("drivers"):
        for route_number in os.listdir(driver):
            coord_to_graph_image("drivers/" + driver + route_number)
    """
