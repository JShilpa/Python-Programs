#Python Program for implementation of matching delimiters in a string

from array_stack import ArrayStack

k = ArrayStack();
leftstring = '{([';
rightstring = '})]';

def matching_delimiter(inputstring):
    for c in inputstring:
        if c in leftstring:
            k.push(c);
        elif c in rightstring:
            if k.is_empty():
                return False;
            elif rightstring.index(c) != leftstring.index(k.pop()):
                return False;

    return k.is_empty();


print(matching_delimiter('[(5+x)-(y+z)]'));
print(matching_delimiter('[(5+x)-(y+z)'));
