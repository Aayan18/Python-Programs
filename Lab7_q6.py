a = str(input('enter a sentence:'))
x=a.split()
l=len(x)
print(a)
for i in range(-1,-l-1,-1):
    print(x[i],end=" ")
    