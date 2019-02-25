#!/usr/bin/env python3
#The greatest common divisor (GCD) of a and b is the largest number that divides 
# both of them with no remainder.

#One way to find the GCD of two numbers is based on the observation 
#that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). 
# As a base case, we can use gcd(a, 0) = a.

#Write a function called gcd that takes parameters a and b 
#and returns their greatest common divisor.

#Credit: This exercise is based on an example from Abelson and Sussman’s Structure 
#and Interpretation of Computer Programs.
def gcd(a,b):
    result = a % b
    if result == 0 and a/b == 1:
        return a
    elif result == 0 and a/b != 1:
        return b
    elif result != 0:
        return gcd(b,result)
def main():
    print(gcd(30,24))
    print(gcd(10,5))
    print(gcd(15,12))
    print(gcd(100,75))
if __name__ == '__main__':
    main()

    a = 30
    b = 24
    result = 6