def run_task1(points_of_interest):
    print("What is the name of the place?")
    name = str(input()).title()
    print("What type of place is it?")
    place = str(input())
    print("What is the postcode?")
    address = str(input())
    print(points_of_interest, "before")
    points_of_interest.append([name, place, address, "5"])
    print(points_of_interest, "after")
    print(f"Added to file")

