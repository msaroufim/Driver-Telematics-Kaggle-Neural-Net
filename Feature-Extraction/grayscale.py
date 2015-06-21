#!/usr/bin/env python

"""
Turn RGB images into grayscale
"""


def main(driver):
    dataset = []
    data_location = "../Keras-nets/drivers/"
    #for driver in os.listdir(data_location):
    path = data_location + driver
    for route_number in os.listdir(path):

        route_filename = path + '/' + route_number
        img = Image.open(route_filename).convert('gray')


        #CHANGE IF NEEDED TO DIFFERENT SIZE, TRY TO KEEP IT SQUARE
        resized_image_name = resize_image_save( coord_to_graph_image(path + '/' + route_number) ,25,25)
        dataset.append([resized_image_name,driver])
        #random.shuffle(dataset) will shuffle it properly in place so no return value
    print '-'*50
    print dataset
    return dataset


if __name__ == "__main__":
    NUM_DRIVERS = 3612
    for i in range(1,NUM_DRIVERS):
        p = multiprocessing.Process(target=main,args=(i,))
        p.start()
