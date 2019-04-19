#!/usr/bin/env python3
def avoids(word, letters):
    for i in letters:
        if i in word:
            return False
        else:
            continue
    return True

user = input("What are the forbidden words?")
find = open('words.txt','r')
wordcount = 0
nonforbidden = 0

letter_v_word = {}

for line in find:
    word = line.strip()

    for letter in set(word):
        if letter not in letter_v_word:
            letter_v_word[letter] = 1
        else: 
            letter_v_word[letter] += 1 
    
    if avoids(word, user):
        # print(word)
        nonforbidden += 1
print('%d words that don\'t have the forbiddened letters.'%(nonforbidden))

print(sorted(letter_v_word.items(), key=lambda kv:(kv[1], kv[0]))[:5])
