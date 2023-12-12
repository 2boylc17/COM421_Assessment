import csv
import math
from Task_3 import quicksort


def run_task5(points_of_interest):
    print("What is the name of the place you would like to book?")
    searchvalue = str(input()).title()
    quicksort(points_of_interest, 0, len(points_of_interest) - 1, 0)
    start = 0
    end = len(points_of_interest) - 1
    found = False
    while found is False:
        middle = math.floor((start + end) / 2)
        if points_of_interest[middle][0] == searchvalue:
            print(f"{searchvalue} is a valid location")
            avail = int(points_of_interest[middle][3])
            points_of_interest[middle][3] = str(avail - 1)
            print(f"New availability is {points_of_interest[middle][3]}")
            print(points_of_interest)
            found = True
        elif start == end:
            print(f"{searchvalue} is not a valid location")
            found = True
        elif points_of_interest[middle][0] > searchvalue:
            end = middle - 1
        elif points_of_interest[middle][0] < searchvalue:
            start = middle + 1
