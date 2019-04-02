#!/usr/bin/env python3
import math
import sys
def square_root(a):
    x = 3.0
    while True: 
        y = (x + a/x)/2
        if abs(y-x) < sys.float_info.epsilon:
            return x
            break
        x = y
b,c,d,e,f,g,h,i,j = 1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0
def test_square_root(z):    
    print("{} \t {} \t {} \t {}".format(z,square_root(z),math.sqrt(z),abs(math.sqrt(z)-square_root(z))))
test_square_root(b)
test_square_root(c)
test_square_root(d)
test_square_root(e)
test_square_root(f)
test_square_root(g)
test_square_root(h)
test_square_root(i)
test_square_root(j)
