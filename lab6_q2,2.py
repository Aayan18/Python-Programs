N = int(input('enter number:'))
sum = 0
fact = 1
i = 1
if N<0:
    print("invalid input:")
elif N==0:
    fact == 1
else :
    for i in range (1,N+1):
        fact = fact*i
        a = 1/fact
        sum = sum+a
print (f'{sum:.9f}')   
            
