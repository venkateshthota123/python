# cook your dish here
x=int(input())
for i in range(x):
    a=input()
    b=input()
    c=""
    for i in range(len(a)):
        if a[i]==b[i]:
            c+="g"
        else:
            c+="b"
    print(c.upper())