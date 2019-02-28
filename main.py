import math


a = 0
b = 2
c = int(input())
while(c < 0):
    print('You have made a mistake')
    c  = int(input())
while(a < b):
    c = c + 1
    a = a + 1

print('Result is ' + str(c))


