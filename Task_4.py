import csv
import math
from Task_3 import quicksort


def run_task4():

    print("What is the type of the place you would like to stay?")
    searchvalue = str(input()).title()
    array = []
    with open("data.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            array.append(values)
    newarr = array
    quicksort(newarr, 0, len(newarr) - 1, 1)
    start = 0
    end = len(array) - 1
    found = False
    while found is False:
        middle = math.floor((start + end) / 2)
        print(start, end, middle)
        print(newarr[middle][1])
        if newarr[middle][1] == searchvalue:
            print(f"{searchvalue} is a valid location")
            for num in range(len(array)):
                if array[num][1] == searchvalue:
                    print(array[num])
            found = True
        elif start >= end:
            print(f"{searchvalue} is not a valid location")
            found = True
        elif newarr[middle][1] > searchvalue:
            end = middle - 1
        elif newarr[middle][1] < searchvalue:
            start = middle + 1
