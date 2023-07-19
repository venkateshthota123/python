# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    b=input().split()
    c=0
    if a<=1:
        print(1)
    else:
        for i in range(1,len(b)):
            if b[0]==b[i]:
                c+=1
        print(c)
            
        
    
        
