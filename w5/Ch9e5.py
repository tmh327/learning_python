#!/usr/bin/env python3

def uses_all(word,letters):
    x = 0
    for letter in letters:
        if letter not in word:
            return False
    return True

print(uses_all('canibecomeanybetter','aieotr')) 
        
