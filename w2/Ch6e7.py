#!/usr/bin/env python3
#A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
#Write a function called is_power that takes parameters 
#a and b and returns True if a is a power of b. 
#Note: you will have to think about the base case.
def is_power(a,b):
    result = a/b
    if result == 1 and a%b == 0:
        return True
    elif a%b != 0:
        return False
    return is_power(result,b)
def main():
    print (is_power(32,2))
    print (is_power(51,3))
    print (is_power(16,3))
if __name__ == '__main__':
    main()