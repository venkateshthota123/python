# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    if b <=4 and a<=1:
        print(1)
    else:
        r=(a*b)/4
        print(math.ceil(r))