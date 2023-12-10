n1 = int(input('enter no. of elements of list 1:'))
n2 = int(input('enter no. of elements of list 2:'))
l1 =[]
l2 =[]

for i in range (0,n1):
    l1.append(int(input('enter no.')))
for j in range (0,n2):
    l2.append(int(input('enter no.')))
set_A=set(l1)
set_B=set(l2)
union = set_A|set_B
intersection = set_A&set_B
difference = set_A-set_B
SD = (set_A - set_B)|(set_B - set_A)
print (union,intersection,difference,SD)
