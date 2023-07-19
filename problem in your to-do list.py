# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    b=input().split()
    c=0
    for i in range(a):
        if len(b[i])==4:
            c+=1
    print(c)
        
