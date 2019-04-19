#!/usr/bin/env python3
def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

find = open('words.txt','r')
print(type(fin))
wordcount = 0
wordhasnoe = 0
for line in find:
    wordcount += 1
    word = line.strip()
    if has_no_e(word):
        wordhasnoe += 1
        print(word)
print('%d percent words with no e.'%(wordhasnoe*100/wordcount))
