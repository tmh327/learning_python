#!/usr/bin/env python3
def find(word,letter,start):
    while start < len(word):
        if word[start] == letter:
            return start    
        else:
            start += 1
    return -1     



def count(string,letter):
    start, count = 0,0   
    while find(string,letter,start) != -1:
        count += 1
        start = find(string,letter,start)+1
    return count
        
print(count('banana','a')) 
