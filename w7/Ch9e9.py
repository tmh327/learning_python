#!/usr/bin/env python3
def fill_string(i, len):
    return str(i).zfill(len)

def are_reverse(x, y):
    return fill_string(x,2) == fill_string(y,2)[::-1]

final_daughter_age = 0
def check(diff):
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        
        if are_reverse(daughter,mother):
            count += 1
            print(daughter,mother)

        if mother > 120:
            break
        daughter += 1
    final_daughter_age = daughter
    return count

def check_age(x):
    diff = 10
    while diff < 70:
        n = check(diff)
        diff += 1
        if n == x:
            return

print(check_age(8))
