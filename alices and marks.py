a,b=input().split(" ")
a=int(a)
b=int(b)

if a==1 or b==1:
    if a > b:
        print('Yes')
    else:
        print('No')
else:
    if a >= 2*b:
        print('Yes')
    else:
        print('No')
