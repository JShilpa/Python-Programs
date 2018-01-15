# Python program for implementing merge sort

def merge(data, start, midpoint, end):
    pass

def mergeSort(data, start, end=None):
    print(end)
    if end is None:
        end = len(data)-1
    if start < end:
        midpoint = start + end // 2
        mergeSort(data, start, midpoint);
        mergeSort(data, midpoint + 1, end)
        merge(data, start, midpoint, end);

mergeSort([5, 10,15,7,9,12], 0)

