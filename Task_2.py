import csv
import math


def run_task2():

    print("What is the name of the place you would like to stay?")
    searchvalue = str(input()).capitalize()
    array = []
    with open("data.csv") as file:
        csv_reader = csv.reader(file)
        for values in csv_reader:
            array.append(values)
    newarr = array
    start = 0
    end = len(array) - 1
    found = False
    while found is False:
        middle = math.floor((start + end) / 2)
        print(start, end, middle)
        if newarr[middle][0] == searchvalue:
            print(f"{searchvalue} is a valid location")
            found = True
        elif start == end:
            print(f"{searchvalue} is not a valid location")
            found = True
        elif newarr[middle][0] > searchvalue:
            end = middle - 1
        elif newarr[middle][0] < searchvalue:
            start = middle + 1