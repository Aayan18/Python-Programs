
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
d=(b**2)-(4*a*c)
if a==0:
    print("equation is invalid")
if d<0:
    print("Imaginary roots")
elif d==0:
    print("Real and equal roots")
    Y=((-b/(2*a)))
    print(Y)
elif d>0:
    print("Real and distinct roots")
    x1=((-b+(d**0.5)/(2*a)))
    x2=((-b-(d**0.5)/(2*a)))
    print("The roots are:", x1,x2)