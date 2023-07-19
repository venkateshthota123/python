
def lunch(x):
    for i in range(len(x)):
        if x[i]>1 and x[i]<4:
            print("YES")
        else:
            print("NO")
a=int(input())
l=[]
for i in range(a):
    l.append(int(input()))
lunch(l)
