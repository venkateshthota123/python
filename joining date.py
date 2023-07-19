# cook your dish here
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split(" "))
    print(math.ceil(a/5)-math.ceil(b/5))
    