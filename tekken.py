# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a-b<0 or a-c<0:
        print("NO")
    else:
        print('YES')