# cook your dish here
x=int(input())
for i in range(x):
    a=input()
    c="sad"
    for i in range(len(a)-2):
        if a[i] in ['a','e','i','o','u']:
            if a[i+1] in ['a','e','i','o','u']:
                if a[i+2] in ['a','e','i','o','u']:
                    c="Happy"
    print(c)