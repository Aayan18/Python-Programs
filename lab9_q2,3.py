n1 = int(input('enter no. of elements of list 1:'))
n2 = int(input('enter no. of elements of list 2:'))
l1 =[]
l2 =[]

for i in range (0,n1):
    l1.append(int(input('enter no.')))
for j in range (0,n2):
    l2.append(int(input('enter no.')))
l3=[]
l4=l1+l2
for k in (l4) :
    if (k not in l1) and (k not in l2):
        l3.append(k)
print(l3)