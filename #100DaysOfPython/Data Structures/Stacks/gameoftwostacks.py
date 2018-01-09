#
from arraystack import ArrayStack

no_of_games = int(input("Enter No of games"));
for i in range(no_of_games):
    stack_data_limit = input("Enter stack A data limit, Enter stack B data limit , Enter not exceed sum");
    stack_values = stack_data_limit.split('');
    stack_a_limit = int(stack_values[0]);
    stack_b_limit = int(stack_values[1]);
    max_sum_limit = int(stack_values[2]);
    stack_data = int(input("Enter stack A data"))
    print(stack_data);
    #for j in range(stack_a_limit):
