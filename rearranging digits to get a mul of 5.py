x=int(input())
for i in range(x):
    a=int(input())
    b=input()
    c=0
    for i in b:
        if i=='0' or i=='5':
            c+=1
    if c>=1:
        print("yes")
    else:
        print("NO")
       