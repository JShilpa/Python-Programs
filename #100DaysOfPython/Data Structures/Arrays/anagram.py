# Python program for implementing anagram check

def checkForAnagram(str1, str2):
    str1_list = list(str1.replace(" ", "").lower())
    str2_list = list(str2.replace(" ",'').lower())

    is_anagram = True
    if len(str1_list) == len(str2_list):
        for i in range(0, len(str1_list)):
            if str1_list[i] in str2_list and str1_list.count(str1_list[i]) == str2_list.count(str1_list[i]):
                pass
            else:
                is_anagram = False
    else:
        print("Not same length. Not an Anagram")

    if(is_anagram):
        print("Is an Anagram")
    else:
        print("Not an Anagram")

    


checkForAnagram('William Shakespeare', 'I am a weakish speller')
