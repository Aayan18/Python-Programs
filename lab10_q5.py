def lift_shifter (list , k):
    n = len(list)
    k = k % n
    shifted_list = list[k:] + list[:k]
    
    return shifted_list
original_list = []
x = int(input('enter length of list:'))
for i in range (x):
    y = int(input('enter elements of list:'))
    original_list.append(y)
k = int(input('enter shift:'))
shifted_list = lift_shifter(original_list , k)
print('Original List:', original_list)
print('Shifted List:', shifted_list)    
