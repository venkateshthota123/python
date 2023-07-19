# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    m=0
    for i in range(1,a+1):
        if a%i==0:
            m+=1
    if m==2:
        print("yes")
    else:
        print("no")