# cook your dish here
x=int(input())
for i in range(x):
    a=int(input())
    if a >1500:
        hra=500
        dsa=a*(98/100)
        basic_salary=a+hra+dsa
        print(basic_salary)
    else:
        hra=a*(10/100)
        dsa=a*(90/100)
        basic_salary=a+hra+dsa
        print(basic_salary)