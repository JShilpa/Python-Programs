# Python Program for learning about sets

a = int(input('Enter number of elements for setM'))
set_nos = input('Enter elements of setM space seperated')
print(len(set_nos.split()))
if len(set_nos) == a:
    list_m = list(map(int, set_nos))
    print(list_m)
else:
    print('Please enter correct numbers of elements for set M')


