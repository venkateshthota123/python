x=int(input())
for i in range(x):
    a,b,c=input().split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    if b>=c and b>=a:
        print('Yes')
    else:
        print('No')