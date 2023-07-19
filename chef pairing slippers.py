# cook your dish here
x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    r=a-b
    print(min(r,b)*c)
   