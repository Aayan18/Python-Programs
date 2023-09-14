N = int(input('enter num:'))
fact =1 
i=1
if N<0:
    print ('invalid input')
elif N==0:
      fact=1
while i<=N:
    fact = fact*i
    i=i+1
print(fact)

    