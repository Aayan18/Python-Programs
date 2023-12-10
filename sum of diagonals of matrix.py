def diagonal_sums(matrix):
    n = len(matrix)
    
    main_diagonal_sum = sum(matrix[i][i] for i in range(n))
    anti_diagonal_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    
    return main_diagonal_sum, anti_diagonal_sum
l =[]
c = int(input('no. of columns:'))
r = int(input('no. of rows:'))
for i in range (0,r):
    l.append([])
    for j in range (0,c):
        l[i].append(0)
        l[i][j]= int(input('enter elements of matrix:'))
print(diagonal_sums(l))

