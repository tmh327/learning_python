#!/usr/bin/python3
'''exercise 5.2'''
def do_n(f,n):
    do_n(n-1)

"""exercise 5.3
Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
an + bn = cn for any values of n greater than 2.

Write a function named check_fermat that takes four parameters—a, b, c 
and n—and that checks to see if Fermat’s theorem holds. 
If n is greater than 2 and it turns out to be true that
    an + bn = cn 
the program should print, “Holy smokes, Fermat was wrong!” 
Otherwise the program should print, “No, that doesn’t work.”
Write a function that prompts the user to input values for a, b, c and n, 
converts them to integers, and uses check_fermat to check 
whether they violate Fermat’s theorem.    """

def check_fermat(a,b,c,n):
    a = int(input('Enter a positive number a:'))
    b = int(input('Enter a positive number b:'))
    c = int(input('Enter a positive number c:'))
    n = int(input('Enter a positive number n:'))
    if n > 2:
        if a*n + b*n == c*n:
            print('Holy smokes, Fermat was wrong!')
        else:
            print('That doesn\'t work.')
    else:
        print('That doesn\'t work.')