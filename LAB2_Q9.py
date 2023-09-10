pi = int(input('enter amt:'))
r = 7.1
t = int(input('enter num:'))
n = int(input('no. of ci in a year:'))
if pi<500 or t<6:
    print ('invalid')
else:
    a = (pi*((1+r/n)**(n*t)))
    print (a)

    