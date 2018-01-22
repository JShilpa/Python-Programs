#Python Program for implementing mising element


def finder(list1, list2):
    missing_el=[]
    for i in range(0, len(list1)):
        if list1[i] not in list2:
            missing_el.append(list1[i])
    return missing_el

result = finder([1, 2, 3, 4, 5], [1, 2, 4])
print(" ".join(map(str, result)))