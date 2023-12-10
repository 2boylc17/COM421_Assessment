import csv


def partition(data, start, end):
    i = start
    j = end
    pivot = data[(start+end)//2][0]
    while True:
        while data[i][0] < pivot:
            i += 1
        while data[j][0] > pivot:
            j -= 1
        if i < j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        else:
            return j


def quicksort(data, start, end):
    if end <= start:
        return "List sorted"
    else:
        # print(data)
        pivot = partition(data, start, end)
        quicksort(data, start, pivot - 1)
        quicksort(data, pivot + 1, end)


def run_task3():
    list1 = []
    with open("data.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            list1.append(values)
    quicksort(list1, 0, len(list1) - 1)
    for num in range(len(list1)):
        print(list1[num])
    # for loop used to print line by line
