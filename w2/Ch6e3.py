#!/usr/bin/env python3
#Use incremental development to write a function called hypotenuse that 
#returns the length of the hypotenuse of a right triangle given 
#the lengths of the two legs as arguments. 
#Record each stage of the development process as you go. 
import math
def hypotenuse(leg1,leg2):
    length = leg1**2 + leg2**2
    length = math.sqrt(length)
    return length
def main():
    print(hypotenuse(3,4))
if __name__ == '__main__':
    main()