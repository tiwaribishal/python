a=input("enter first side of traingle :")
b =input("enter second side  of traingle:")
c=input("enter third side  of traingle :")
a=float(a)
b=float(b)
c =float(c)

s=(a+b+c)/2


area= (s*(s-a)*(s-b)*(s-c))
print("area of traingle is:",area)