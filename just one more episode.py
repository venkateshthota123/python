# cook your dish here
def episode(x):
    for i in range(x):
        a=int(input())
        if a>24:
            print("Yes")
        else:
            print('No')
n=int(input())
episode(n)