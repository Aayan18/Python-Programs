num = int(input('enter num:'))
sum=0
while (num!=0):
    sum = sum + (num%10)
    num=num//10
print (sum)   
if sum%3==0:
    print('divisible')
else:
    print('not divisible')
