def run_task1():
    print("What is the name of the place?")
    name = str(input())
    print("What type of place is it?")
    place = str(input())
    print("What is the postcode?")
    address = str(input())
    with open("data.csv", "a") as file:
        file.write(f"\n{name},{place},{address}")
    print(f"Added to file")
