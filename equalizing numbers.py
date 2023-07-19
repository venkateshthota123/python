# cook your dish here
x=int(input())
for i in range(x):
    a,b=map(int,input().split(' '))
    if a%2==0 and b%2==0:
        print("yes")
    elif a%2!=0 and b%2!=0:
        print("yes")
    else:
        print("no")