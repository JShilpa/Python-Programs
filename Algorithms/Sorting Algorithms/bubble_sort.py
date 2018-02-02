# Python program for implementation of Bubble Sort, Optimized Bubble Sort & Recursive Bubble Sort


# Bubble Sort with nested for-loops.
# Worst and Average Case Time Complexity: O(n^2)

def bubble_sort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(0, n-i-1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


# Optimized Implementation for Sorted Array List
# Best Case Time Complexity: O(n).

def optimal_bubble_sort(alist):
    n = len(alist)
    swapped = False

    for i in range(n):
        for j in range(0, n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                swapped = True

    # If inner loop doesn't swap any element in first iteration, break the loop
        if swapped is False:
            break


# Recursive Bubble Sort

def recursive_bubble_sort(alist, step=None):
    n = len(alist)
    if step is None:
        step = 0
    swapped = False
    if n is 1:
        return False

    for i in range(n-step-1):
        if alist[i] > alist[i + 1]:
            alist[i], alist[i + 1] = alist[i + 1], alist[i]
            swapped = True
    step+=1
    if swapped is True:
        recursive_bubble_sort(alist)



# Bubble Sort Test.
# Complexity: 0(n^2)

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(alist)   # In Place Algorithm

# Optimized Bubble Sort Test.
# Complexity: 0(n).

arr = [1, 2, 3, 4, 5]
optimal_bubble_sort(arr)
print(arr);

# Recursive Bubble Sort Test.
# Complexity: 0(n^2)

alist = [-2, 4, 5, -11, 9, -10]
recursive_bubble_sort(alist)
print(alist)