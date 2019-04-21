#!/usr/bin/env python3
def uses_only(word,letters):
    for letter in word:
        if letter not in letters:
                return False
    return True
print(uses_only('hoealfalfa','acefhlo'))
print(uses_only('hoealfalfakdao','acefhlo')) 
