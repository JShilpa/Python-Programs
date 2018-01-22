# Python Program for implementing factorial of the number

def getFactorial(number):
    if number == 0:
        return 1
    else:
        return number * getFactorial(number - 1)

factorialValue = getFactorial(int(input("Enter number")))
print(factorialValue);
