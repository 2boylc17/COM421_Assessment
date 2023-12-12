def partition(data, start, end, num):
    i = start
    j = end
    pivot = data[(start+end)//2][num]
    while True:
        while data[i][num] < pivot:
            i += 1
        while data[j][num] > pivot:
            j -= 1
        if i < j and data[i][num] != data[j][num]:
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


def run_task3(points_of_interest):
    quicksort(points_of_interest, 0, len(points_of_interest) - 1, 0)
    for num in range(len(points_of_interest)):
        print(points_of_interest[num])
    # for loop used to print line by line
