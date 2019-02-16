#!/usr/bin/python3
"""exercise 2"""
width = 17
height = 12.0
delimeter = '.'
print (width/2,'\n',width/2.0,'\n',height/3,'\n',1+2*5,'\n',delimeter*5)

"""exercise 3"""
r = 5
volume = 4/3*r**3
print('1.',format(volume,'.2f'))

price = 24.95 * 0.6
price = price + 3 + (price + 0.75) * 59 
print('2.',format(price,'.2f'),'$')

hour = 60
minute = 60
sec = 1
time = 6 * hour * minute + 52 * minute
easy = 8 * minute + 15
tempo = (7 * minute + 12) * 3
hourdigit = (time + easy + tempo)/(hour * minute)
print('3',format(hourdigit,'.2f'))