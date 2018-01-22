# Python program for implementing recursive digit sum

def digitSum(number, times):
    input = number * times
    sum = 0
    input_list = [int(x) for x in input]
    if len(input_list) > 1:
       for i in range(0, len(input_list)):
            sum = sum + input_list[i]
       return digitSum(str(sum), 1)
    else:
        return input

n,k = input("Enter number n and k").strip().split()
n, k = [str(n), int(k)]
result = digitSum(n, k)
print(result)





