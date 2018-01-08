#

from arraystack import ArrayStack
def  max_el():
    pass

def add(e):
    #print(e);
    k.push(e);
    print(k.getitem())

def pop():
    k.pop()
    print(k.getitem())

def max_element():
    pass

k = ArrayStack();
input_number = int(input('Enter a value: '))
for i in range(input_number):
    no_input = input('Enter a inner value: ')
    case_no = no_input.split()
    #print(type(case_no[0]));
    operation = {
             '1': add(int(case_no[1])),
             '2': pop(),
             '3': max_element()
         }.get(case_no[0]);
    #perform_stack_op(case_no)
