"""
List comprehension creates a new list by applying expression to each element of the iterable
[<expression> for <element> in <iterable>]
There is an optional if condition where element is appended to expression when condition evaluates to true
[<expression> if <condition> else <statement>  for <element> in <iterable>]
If/else clause should be used before for loop
"""

# Creating a list of squared integers
squares = [x * x for x in (1, 2, 3, 4)]
print(squares)        # [1, 4, 9, 16]

# Above list comprehension is roughly equivalent to the following for-loop:
squares = []
for x in (1,2, 3, 4):
    squares.append(x * x)
print(squares)       # [1, 4, 9, 16]

# Get a list of uppercase characters from string
str = [s.upper() for s in 'hello' if s == 'h']
print(str)           # ['H', 'E', 'L', 'L', 'O']

# If-else example. It comes before For loop
str = [s if s in 'arial' else '*' for s in 'apple']
print(str)           # ['a', '*', '*', 'l', '*']







