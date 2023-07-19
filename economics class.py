# cook your dish here

x=int(input())
for i in range(x):
    c=0
    a=int(input())
    si=input().split()
    di=input().split()
    for i in range(a):
        if si[i]==di[i]:
            c+=1
    print(c)
