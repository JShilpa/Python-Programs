#Python program for implementing array pair sum and printing unique pairs

def pairSum(iterable_list, value):
    pair =[];
    for i in range(0, len(iterable_list)):
        for j in range(i, len(iterable_list)-1):
            if iterable_list[j] + iterable_list[j + 1] == value and [iterable_list[j], iterable_list[j+1]] not in pair:
                pair.append([iterable_list[j], iterable_list[j+1]])

    print(pair)

pairSum([1,3, 2, 2, 4, 0], 4)

