#
def insertion_sort(a):
    for i in range(1,len(a)):

        j = i-1;
        key = a[i];
        print(j);
        while a[j] > key and j >= 0:
            a[j + 1] = a[j]
            a[j] = key;
            j = j - 1;

        print(alist);


alist = [14, 11, 13, 5, 6];
insertion_sort(alist);