#!/usr/bin/env python3
def is_abecedarian(word):
    for i in range(len(word)-1):
        if ord(word[i]) > ord(word[i+1]):
            return False
    return True

find = open('words.txt','r')
count = 0
for i in find: 
    words = i.strip()
    if is_abecedarian(words):
        count += 1
print('There are %s abecedarian words.'% (count))

