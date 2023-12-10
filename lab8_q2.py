n = int(input("enter (length of list of integers):"))
l=[]
for i in range(n):
    l.append(int(input("enter a integer: ")))
print(l)
l2=[]
for j in range (0,n):
    m=min(l)
    l2.append(m)
    l.remove(m)
print(l2)
    
