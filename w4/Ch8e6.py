#!/usr/bin/env python3
def find(word,letter,start):
    while start < len(word):
        if word[start] == letter:
            return start
        start += 1
    return -1
def count(string,letter,findcount):
    start = 0 
    while start < len(string):
        if string[count] == letter:
            count += 1
    return 
