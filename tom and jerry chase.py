# cook your dish here
n=int(input())
for i in range(n):
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    if b>a:
        print('YES')
    else:
        print("NO")