# cook your dish here
x=int(input())
for i in range(x):
    c=0
    a=input().split()
    for i in range(len(a)):
        if a[i]=="1":
            c+=1
    if c>3:
        print("yes")
    else:
        print("no")
        