import csv
import math
from Task_3 import quicksort


def run_task4(points_of_interest):

    print("What is the type of the place you would like to stay?")
    searchvalue = str(input()).title()
    newarr = points_of_interest
    quicksort(newarr, 0, len(newarr) - 1, 1)
    start = 0
    end = len(points_of_interest) - 1
    found = False
    while found is False:
        middle = math.floor((start + end) / 2)
        if newarr[middle][1] == searchvalue:
            print(f"{searchvalue} is a valid location")
            for num in range(len(points_of_interest)):
                if points_of_interest[num][1] == searchvalue:
                    print(points_of_interest[num])
            found = True
        elif start >= end:
            print(f"{searchvalue} is not a valid location")
            found = True
        elif newarr[middle][1] > searchvalue:
            end = middle - 1
        elif newarr[middle][1] < searchvalue:
            start = middle + 1
