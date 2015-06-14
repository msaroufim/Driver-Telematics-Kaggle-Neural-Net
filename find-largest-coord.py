if __name__ == "__main__":
    for driver in os.listdir("drivers"):
        for route_number in os.listdir(driver):
            file_name = "drivers/" + driver + route_number
            with open(file_name) as f:
                next(f)
