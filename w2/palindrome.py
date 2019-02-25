#!/usr/bin/env python3
def is_palindrome(word):
    if len(word)<=1:
        return True
    elif first(word)!=last(word):
        return False
    return is_palindrome(middle(word))
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def main():
    print (is_palindrome('noon'))
    print (is_palindrome('alila'))
    print (is_palindrome('yoilsoy'))
if __name__ == '__main__':
    main()
