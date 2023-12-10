import csv

print("What is the name of the place you would like to stay?")
name = str(input())
array = []
with open("data.csv") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)
    for values in csv_reader:
        array.append(values)
        print(array)
