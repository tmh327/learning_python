#!/usr/bin/env python3
def check(num):
    x = len(num)-1
    count = 0
    for i in range(len(num)-1):
        print(i,x)
        if num[i] == num[x]:
            print (num[i],num[x])
            x -= 1
            count += 1
            if num[i+1] != num[x]:
                print(num[i],num[x])
                return False     
            if i == x:
                break
        else:
            count = 0
    if count >= 2:
        return True
    else:
        return False

print(check('121121'))
print(check('123231'))
for i in range(100000,1000000):
    if check(str(i)):
        print(i)
    
