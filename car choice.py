# cook your dish here
x=int(input())
for i in range(x):
    l1,l2,x1,x2=map(int,input().split())
    c1=x1/l1
    c2=x2/l2
    if c1==c2:
        print(0)
    elif c1>c2:
        print(1)
    else:
        print(-1)