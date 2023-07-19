# cook your dish here

def palindrome(x):
    for i in range(x):
        a=input()
        b=a[::-1]
        
        if a==b:
            print("wins")
        else:
            print("loses")
x=int(input())
palindrome(x)