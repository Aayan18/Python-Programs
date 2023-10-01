N = int(input('enter number:'))
x = float(input('enter number for division:'))
sum = 1
for i in range (1,N+1):
    F = x**i
    a = F/i
    sum = sum+a
print (f'{sum:.9f}')

