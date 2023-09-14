a= int(input('enter number:'))
s = str(a)
l= len(s)
i=0
sum=0
while l>i:
    dij = a%10
    sum=sum+dij
    a=a//10
    i=i+1
print(sum)


