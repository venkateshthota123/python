temp=input("enter the temperature to convert(ex 23 c or 23 f):")
unit=temp[-1]
val=float(temp[:-1]).replace(" ","")
if unit=='c' or unit=='C':
    f=(9/5)*val+32
    print(f"{temp} degrees celius ={f} degrees faranheit")
elif unit=='f'or unit=='F':
    c=(5/9)*val-32
    print(f"{temp} degrees faranheit={c} degrees celius")
else:
    print("enter correct value")
