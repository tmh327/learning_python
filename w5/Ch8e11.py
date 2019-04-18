#!/usr/bin/env python3
def any_lowercase1(s):
#check if there is any lower case in the string
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
#logic error so it doesn't check if there is any lower case but rather it checks if "c" is a lower case letter
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
#checking if the last letter of the string is a lower case
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
#check if there is any lower case in the string
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
#correct function
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5("uppercase"))
