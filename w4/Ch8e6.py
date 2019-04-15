#!/usr/bin/env python3
def count(string,letter,start):
    c = 0 
    while start < len(string):
        if string[start] == letter:
            c += 1 
        else:
            c = c
        start += 1   
    return print(c)
        
count('hubbub','b',3)
