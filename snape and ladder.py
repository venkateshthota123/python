# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split(" "))
    c=math.sqrt(a*a+b*b)
    d=math.sqrt(b*b-a*a)
    print(round(d,4),round(c,4))
