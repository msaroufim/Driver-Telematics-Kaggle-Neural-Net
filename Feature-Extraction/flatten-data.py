"""
A helper script that takes in data of the form
Input:
data
    --1
        --1.csv: [x_1,y_1] ... [x_n,y_n]
        ...
        --200.csv
    ...
    --1700

And turns it into the following single csv file
Output:
[x_i, y_i, route_j, driver_k]

Each one of those values will be fed into a neural network by first uniformily at random picking a driver, then a route and the whole sequence for a given route is fed to the network sequentially.


"""
