n = int(input("enter (length of list of integers):"))
l=[]
sum = 0 
product = 1
for i in range(n):
    l.append(int(input("enter a integer: ")))
s = []
for i in l:
    if i not in s:
        s.append(i)
print(s)
        