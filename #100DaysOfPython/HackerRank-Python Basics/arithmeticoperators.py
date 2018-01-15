# Python program for implementing arithemetic operations
# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# https://www.hackerrank.com/challenges/python-division/problem
# https://www.hackerrank.com/challenges/python-loops/problem

def performOperations(number1, number2):
    print(number1 + number2)
    print(number1 - number2)
    print(number1 * number2)
    print(number1 / number2)   # Float Division
    print(number1 // number2)  # Integer Division
    for i in range(number1):
        print(i ** 2)          # Squaring

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    performOperations(a, b)
