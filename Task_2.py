import math
from Task_3 import quicksort


def run_task2(points_of_interest):

    print("What is the name of the place you would like to stay?")
    searchvalue = str(input()).title()
    newarr = points_of_interest
    quicksort(newarr, 0, len(newarr) - 1, 0)
    start = 0
    end = len(points_of_interest) - 1
    found = False
    while found is False:
        middle = math.floor((start + end) / 2)
        # print(start, end, middle)
        if newarr[middle][0] == searchvalue:
            print(f"{searchvalue} is a valid location")
            print(newarr[middle])
            found = True
        elif start >= end:
            print(f"{searchvalue} is not a valid location")
            found = True
        elif newarr[middle][0] > searchvalue:
            end = middle - 1
        elif newarr[middle][0] < searchvalue:
            start = middle + 1
