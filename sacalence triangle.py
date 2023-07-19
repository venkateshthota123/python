# cook your dish here
def scalence(x):
    for i in range(x):
        a,b,c=input().split(" ")
        if a==b or a==c or b==c:
            print("NO")
        else:
            print("YES")
x=int(input())
scalence(x)