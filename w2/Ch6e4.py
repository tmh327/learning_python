#!/usr/bin/env python3
#Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.
def is_between(x,y,z):
    return x<=y<=z
def main():
    print(is_between(1,2,3))
if __name__ == '__main__':
    main()