# cook your dish here
def fillwater(x):
    for i in range(x):
        a,b=input().split(" ")
        a=int(a)
        b=int(b)
        c=a-b
        print(c)
x=int(input())
fillwater(x)