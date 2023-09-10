#a*x**2+b*x+c
a = int(input('enter num:'))
b = int(input('enter num:'))
c = int(input('enter num:'))
d = b**2 -(4*a*c)
val1 = (-b + (d**0.5))/2*a
val2 = (-b -(d**0.5))/2*a
val3 = -b/(2*a)
if d <0:
    print('roots are imaginary')
elif d==0:
    print('roots are real and equal',val3)
else :
    print('roots are real and distinct',val1,val2)
    

