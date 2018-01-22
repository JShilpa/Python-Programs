# Python program to implement binary search on sorted array list using Recursion

def binarySearch(data, target, low=0, high=None):
    if high is None:
        high = len(data)-1
    if low > high :
        return False
    else:
        mid = (low + high)// 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
           return binarySearch(data, target, low, mid-1)
        else:
            return binarySearch(data,target, mid+1, high)

elementFound = binarySearch([2,10, 14, 16, 20, 22, 90, 100], 100, 0, 7)
print(elementFound)
