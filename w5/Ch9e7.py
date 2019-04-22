#!/usr/bin/env python3 
def triple_double(word):
    count = 0
    i = 0
    while i < (len(word)-1):
        if count == 3:
            return True
        if word[i] == word[i+1]:
            count += 1
            i += 2
        else:
            count = 0
            i+=1
        
    return False
def findtriple(wordfile):
    txt = open(wordfile,'r')
    for i in txt:
        words = i.strip()
        if triple_double(words):
            return words

print(findtriple('words.txt')) 
