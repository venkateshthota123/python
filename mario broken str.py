# cook your dish here
x=int(input())
for i in range(x):
    n=int(input())
    s=input()
    val=n//2
    if s[:val]==s[val:]:
        print("YES")
    else:
        print("NO")
   