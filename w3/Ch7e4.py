#!/usr/bin/env python3
import math
def eval_loop():
    while True:
        x = input('Please input an equation:')
        if x == "done":
            break
        print(eval(x))
eval_loop()    
