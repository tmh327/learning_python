#!/usr/bin/python3
'''exercise 3'''
def right_justify(s):
    print(' '*(70-len(s)),s,sep='')
    return
right_justify('allen')

'''
1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, 
a function object and a value, 
and calls the function twice, passing the value as an argument.
3.Write a more general version of print_spam,
called print_twice, that takes a string as a parameter and prints it twice.
4.Use the modified version of do_twice to 
call print_twice twice, passing 'spam' as an argument.
5.Define a new function called do_four that takes a function object
and a value and calls the function four times, passing the value as a parameter.
There should be only two statements in the body of this function, not four.
'''
'''exercise 4.1'''
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
do_twice(print_spam)

'''exercise 4.2'''
def do_twice1(f,g):
    f(g)
    f(g)

'''exercise 4.3'''
def print_twice(s):
    print(s)
    print(s)

'''exercise 4.4'''
def do_twice2():
    print_twice('spam')
    print_twice('spam')

'''exercise 4.5'''
def do_four(f,g):
    do_twice1(f,g)
    do_twice1(f,g)
do_four(print_twice,'spam')

"""exercise 5.1
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""
def printpic():
    plus = "+"
    dash = "-"
    space = " "
    print((plus + space + (dash + space)*4)*2 + plus)
    print('+ ','- '*4,'+ ','- '*4,'+',sep='')
    print('| ','  '*4,'| ','  '*4,'|',sep='')
    print('| ','  '*4,'| ','  '*4,'|',sep='')
    print('| ','  '*4,'| ','  '*4,'|',sep='')
    print('| ','  '*4,'| ','  '*4,'|',sep='')

def main():
    do_twice(printpic)
    print('+ ','- '*4,'+ ','- '*4,'+',sep='')


if __name__ == '__main__':
    main()



