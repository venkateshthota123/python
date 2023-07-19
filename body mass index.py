# cook your dish here
x=int(input())
for i in range(x):
    m,h=map(int,input().split())
    bmi=m/(h*h)
    if bmi<=18:
        print(1)
    elif bmi in range(19,25):
        print(2)
    elif bmi in range(25,30):
        print(3)
    else:
        print(4)
    