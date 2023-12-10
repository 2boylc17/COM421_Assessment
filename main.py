from Task_1 import run_task1
from Task_2 import run_task2
from Task_3 import run_task3
from Task_4 import run_task4
from Task_5 import run_task5


def run_task():
    print(f"What would you like to do?\n"
          f"[1] - Add a new place to stay\n"
          f"[2] - Search for a specific place to stay\n"
          f"[3] - Display all places to stay\n"
          f"[4] - Search for a type of place to stay\n"
          f"[5] - Make a booking for a place to stay\n"
          f"[6] - Exit")
    num = input()
    if num == '1':
        run_task1()
        input("(Press Enter)")
        run_task()
    if num == '2':
        run_task2()
        input("(Press Enter)")
        run_task()
    if num == '3':
        run_task3()
        input("(Press Enter)")
        run_task()
    if num == '4':
        run_task4()
        input("(Press Enter)")
        run_task()
    if num == '5':
        run_task5()
        input("(Press Enter)")
        run_task()
    if num == '6':
        print("Thank you")
    else:
        print("Input not recognised")
        input("(Press Enter)")
        run_task()


run_task()
