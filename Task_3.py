import csv


def partition(data, start, end, num):
    i = start
    j = end
    pivot = data[(start+end)//2][num]
    while True:
        while data[i][num] < pivot:
            i += 1
        while data[j][num] > pivot:
            j -= 1
        if i < j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        else:
            return j


def quicksort(data, start, end, num):
    if end <= start:
        return "List sorted"
    else:
        # print(data)
        pivot = partition(data, start, end, num)
        quicksort(data, start, pivot - 1, num)
        quicksort(data, pivot + 1, end, num)


def run_task3():
    list1 = []
    with open("data.csv") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for values in csv_reader:
            list1.append(values)
    quicksort(list1, 0, len(list1) - 1, 0)
    for num in range(len(list1)):
        print(list1[num])
    # for loop used to print line by line
