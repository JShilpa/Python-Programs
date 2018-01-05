# Python program for implementation for Bubble Sort

def bubble_sort(alist):

   #Traverse through all the array elements.
    for i in range(0, len(alist)):
        for j in range(0,len(alist)-i-1):
            if(alist[j] > alist[j + 1]):
                temp = alist[j];
                alist[j] = alist[j+1];
                alist[j+1] = temp;

alist = [54,26,93,17,77,31,44,55,20];
bubble_sort(alist);
print(alist);