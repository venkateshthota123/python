x=int(input())
for i in range(x):
    a=input().split()
    b=input().split()
    a="".join(a)
    b="".join(b)
    s1=a.count("1",0,len(a))
    s2=b.count("1",0,len(b))
    if s1==s2:
        print("Pass")
    else:
        print("Fail")
