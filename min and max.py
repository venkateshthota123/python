# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    b=list(map(int,input().split()))
    mi=min(b)
    c=0
    if a==1:
        print(0)
    else:
        for i in range(a):
            if mi!=b[i]:
                c+=1
        print(c)