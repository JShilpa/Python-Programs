# Python program to check for Leap Year

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    elif year % 100 == 0 and year % 400 == 0:
        leap = True
    return leap


year = int(input("Enter the year"))
print(is_leap(year))