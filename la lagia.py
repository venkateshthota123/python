x=int(input())
for i in range(x):
    e=0
    m=0
    r=0
    b=0
    for j in range(4):
        dic=input().split()
        if "Barcelona" in dic:
            b=int(dic[1])
        elif "Malaga" in dic:
            m=int(dic[1])
        elif "RealMadrid" in dic:
            r=int(dic[1])
        else:
            e=int(dic[1])
    if r<m and b>e:
        print("Barcelona")
    else:
        print("RealMadrid")
        