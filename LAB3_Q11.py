num = int(input('enter num:'))
sum=0
x = num 
while x>0:
    dig = x%10
    sum = sum + dig**3
    x = x//10
if num==sum:
    print('num is armstrong')
else:
    print('number is not armstrong')
            