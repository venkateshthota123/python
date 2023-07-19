# cook your dish here
x=int(input())
for i in range(x):
    a,b,c,d=map(int,input().split())
    if a==c or b==d:
        print("YES")
    else:
        print("NO")