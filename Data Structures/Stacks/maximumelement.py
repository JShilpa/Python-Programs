#

from arraystack import ArrayStack
def  max_el():
    #print(max(k.getitem()));
    items = k.getitem();
    max_el = items[0];
    for i in items:
        if max_el < i:
            max_el = i;

    print(max_el);

def add(e):
    #print(e);
    k.push(e);
    #print(k.getitem())

def remove():
    k.pop()
    #print(k.getitem())

k = ArrayStack();
input_number = int(input())
for i in range(input_number):
    no_input = input()
    case_no = no_input.split()
    #print((case_no[0]));
    operation = {
             '1': add,
             '2': remove,
             '3': max_el
                }
    if case_no[0] == '1':
       operation[case_no[0]](int(case_no[1]))
    else:
        #print(case_no[0])
        operation[case_no[0]]()

    #perform_stack_op(case_no)
