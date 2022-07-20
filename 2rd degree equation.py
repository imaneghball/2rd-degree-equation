import math
print("you habe aX^2+bX+c")
a=float(input("plese enter a :"))
b=float(input("plese enter b :"))
c=float(input("plese enter c :"))
delta=b**2-(4*a*c)
if delta>0:
    print("2")
    res1=(-b+math.sqrt(delta))/2*a
    res2=(-b-math.sqrt(delta))/2*a
    print(f"X1 = {res1}\nX2 = {res2}")
if delta==0:
    print("1")
    res=-b/(2*a)
    print(f"X0 = {res}")
if delta<0:
    print("0")
