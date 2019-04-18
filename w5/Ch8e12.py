#!/usr/bin/env python3
def rotate_letter(letter,i):
    if letter.isupper():
        begin = ord("A")
    elif letter.islower():
        begin = ord("a")
    else:
        return letter

    char1 = ord(letter) - begin
    char2 = (char1 + i)%26 + begin
    return chr(char2)
def rotate_word(word,i):
    new = ''
    for w in word:
        new += rotate_letter(w,i)
    return new

if __name__ == '__main__':
    print (rotate_word('cheer', 7))
    print (rotate_word('melon', -10))
    print (rotate_word('sleep', 9))

