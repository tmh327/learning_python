#!/usr/bin/env python3

def is_palindrome(word):
    if word[:] == word[::-1]:
        return True
    else:   
        return False

print(is_palindrome('noon'))
print(is_palindrome('redivider'))
print(is_palindrome('haha'))
