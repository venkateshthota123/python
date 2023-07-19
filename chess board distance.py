# cook your dish here
x=int(input())
for i in range(x):
    x1,y1,x2,y2=map(int,input().split())
    x=abs(x1-x2)
    y=abs(y1-y2)
    c=max(x,y)
    print(c)
