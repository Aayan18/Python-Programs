N = int(input('enter number:'))
sum = 0
for i in range (1,N+1):
    a = 1/i   
    sum = (sum + a)
print (f'{sum:.9f}')
