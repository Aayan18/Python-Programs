l =[]
c = int(input('no. of columns:'))
r = int(input('no. of rows:'))
for i in range (0,r):
    l.append([])
    for j in range (0,c):
        l[i].append(0)
        l[i][j]= int(input('enter elements of matrix:'))
print(l)

 

    

