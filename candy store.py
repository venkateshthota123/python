n=int(input())

for i in range(n):
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    if a==b:
        print(a)
    elif a >b:
        print(b)
    else:
        print(a+(b-a)*2)
        
