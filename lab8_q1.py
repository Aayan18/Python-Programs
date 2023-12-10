n = int(input("enter (length of list of integers):"))
l=[]
sum = 0 
product = 1
for i in range(n):
    l.append(int(input("enter a integer: ")))
for i in (l):
    sum = sum + i
for j in l:
    product=product*j
print()
print(f"the list of the integers: {l}")
print(f"the sum of the elements is: {sum}")
print(f"the product of the elements is: {product}")
max=l[0]
for x in l:
    if x>max:
        max=x
print(max)


