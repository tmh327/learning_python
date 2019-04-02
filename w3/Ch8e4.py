#!/usr/bin/env python3
def find(word,letter,start):
    while start < len(word):
        if word[start] == letter:
            return start
        start += 1
    return -1

print(find('Trang','a',2))
print(find('Jesse','e',2))

