# Python program for implmemting anagram using dictionary

def anagram(str1, str2):
    count = {}
    str_1 = str1.replace(" ", '').lower()
    str_2 = str2.replace(" ", '').lower()

    if len(str_1) != len(str2):
        return False

    for letter in str_1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str_2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k0 in count:
        if count[k0] != 0:
            return False

    return True

print(anagram('dog', 'god'))