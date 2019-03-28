#!/usr/bin/env python3
epsilon = 0.000000000000001
def square_root(a):
    x = 3.0
    while True: 
        y = (x + a/x)/2
        if abs(y-x) < epsilon:
            print (x)
            break
        x = y
square_root(25)
square_root(16)
square_root(4) 
