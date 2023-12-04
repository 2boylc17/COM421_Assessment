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
        print("What is the name of the place?")
        name = str(input())
        print("What type of place is it?")
        place = str(input())
        print("What is the postcode?")
        address = str(input())
        with open("data.csv", "a") as file:
            file.write(f"\n{name},{place},{address}")
        print(f"Added to file")


run_task()
