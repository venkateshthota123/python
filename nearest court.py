# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split(" "))
    z=(a+b)/2
    c=max(a-z,b-z)
    print(math.ceil(c))