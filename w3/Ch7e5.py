#!/usr/bin/env python3
import math
def factorial(n):
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)
def estimate_pi():
    k = 0    
    factor = 2 * math.sqrt(2) / 9801
    total = 0
    while True:
        num = factorial(4*k) * (1103+26390*k)
        den = (factorial(k)**4) * (396**(4*k))
        term = factor * num/den
        total += term 
        if abs(term) < 1e-15:
            break
        k += 1 
    return 1/total
print (estimate_pi())
print (math.pi)
