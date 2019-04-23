#!/usr/bin/env python3
def check(num):
    x = len(num)-1
    print(x)
    count = 0
    for i in range(len(num)):
        print(i)
        if num[i] == num[x]:
            print(num[i])
            print(num[x])
            x -= 1
            count += 1
            print('good')
        else:
            count = 0
    print(count)
    #if count >= 2:
     #   return True
    #else: 
     #   return False
check('912421')
#for i in range(100000,1000000):
 #   if check(str(i)):
  #      print(i)
    
