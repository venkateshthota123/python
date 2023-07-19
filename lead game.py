# cook your dish here
x=int(input())
m1=0
m2=0
play1=0
play2=0
for i in range(x):
    a,b=map(int,input().split())
    m1+=a
    m2+=b
    if m1 >m2:
        play1=max(play1,m1-m2)
    else:
        play2=max(play2,m2-m1)
if play1>play2:
    print(1,play1)
else:
    print(2,play2)
        
    