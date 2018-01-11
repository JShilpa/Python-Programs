#
from arraystack import ArrayStack

def max_score(a, b, sum):
    max_val=0;
    j = 0;
    flag = True
    if a[0] < sum:
            for i in a:
                if flag:
                    if a[i] < sum:
                        if a[i] + a[i + 1] < sum and a[i] + a[i + 1] < a[i] + b[j]:
                            a.pop();
                            max_value= max_val + 1;
                        elif a[i] + a[i + 1] < sum and a[i] + a[i + 1] > a[i] + b[j]:
                            b.pop()
                            j = j + 1
                            max_value = max_val + 1;
                    else:
                        flag = False;
                else:
                    for x in b:
                        if b[x] < sum:
                            if b[x] + a[x + 1] < sum:
                                  max_value = max_val + 1;
                            elif a[i] + a[i + 1] < sum and a[i] + a[i + 1] > a[i] + b[j]:
                                b.pop()
                                j = j + 1
                                max_value = max_val + 1;
                        else:
                            print("sum is highest");
                            break


    elif b[0] < sum:
         pass;
    else:
         print("sum is highest")



no_of_games = int(input("Enter No of games"));
for i in range(no_of_games):
    stack_data_limit = input("Enter stack A data limit, Enter stack B data limit , Enter not exceed sum");
    stack_values = stack_data_limit.split();
    stack_a_limit = int(stack_values[0]);
    stack_b_limit = int(stack_values[1]);
    max_sum_limit = int(stack_values[2]);
    stack_a_data = input("Enter stack A data")
    stack_a_list = [int(x) for x in stack_a_data.split()]
    print(stack_a_list);
    stack_b_data = input("Enter stack B data")
    stack_b_list = [int(x) for x in stack_b_data.split()]
    print(stack_b_list);
    max_score(stack_a_list, stack_b_list, max_sum_limit);
    # for j in range(stack_a_list):
    #     print(j)
