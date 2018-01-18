# Python program for implementing printing array in reverse order
# https://www.hackerrank.com/challenges/arrays-ds/problem

def reverseArray(arr, array_size):
    #print(list(reversed(arr)))
    rev_array=[] * array_size

    for i in range(array_size-1, -1, -1):
         rev_array.append(arr[i])

    return rev_array

n = int(input("Enter array size"))
arr = [int(array_temp)for array_temp in input("enter elements").strip().split()]
result = reverseArray(arr, n)
#print(" ".join(map(str, result)))