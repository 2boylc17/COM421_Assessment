import csv

with open("data.csv") as file:
    csv_reader = csv.reader(file)
    headings = next(csv_reader)
    for values in csv_reader:
        print(values)
