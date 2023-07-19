n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        st=str(i)
        if st[len(st)-1] in ['2','3','9']:
            c+=1
    print(c)
        
    
   
   