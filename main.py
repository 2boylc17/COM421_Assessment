from Task_1 import run_task1
from Task_2 import run_task2
from Task_3 import run_task3
from Task_4 import run_task4
from Task_5 import run_task5
import csv

points_of_interest = []
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for values in csv_reader:
        points_of_interest.append(values)


def run_task():
    print(f"\nWhat would you like to do?\n"
          f"[1] - Add a new place to stay\n"
          f"[2] - Search for a specific place to stay\n"
          f"[3] - Display all places to stay\n"
          f"[4] - Search for a type of place to stay\n"
          f"[5] - Make a booking for a place to stay\n"
          f"[6] - Exit")
    num = input()
    if num == '1':
        run_task1(points_of_interest)
        input("(Press Enter)")
        run_task()
    if num == '2':
        run_task2(points_of_interest)
        input("(Press Enter)")
        run_task()
    if num == '3':
        run_task3(points_of_interest)
        input("(Press Enter)")
        run_task()
    if num == '4':
        run_task4(points_of_interest)
        input("(Press Enter)")
        run_task()
    if num == '5':
        run_task5(points_of_interest)
        input("(Press Enter)")
        run_task()
    if num == '6':
        print("Thank you")
        print(points_of_interest)
        with open("data.csv", "w") as file:
            file.write("name,type,location,availability\n")
            for num in range(len(points_of_interest)):
                file.write(f"{points_of_interest[num][0]},{points_of_interest[num][1]},{points_of_interest[num][2]},{points_of_interest[num][3]}\n")
        exit()
    else:
        print("Input not recognised")
        input("(Press Enter)")
        run_task()


run_task()
