def good(x):
    for i in range(x):
        a,b=input().split(" ")
        a=int(a)
        b=int(b)
        if a+b > 6:
            print("YES")
        else:
            print("NO")
good(int(input()))
    
