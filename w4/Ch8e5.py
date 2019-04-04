#!/usr/bin/env python3

def count(string,letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return print(count)
 
count('banana','a')
