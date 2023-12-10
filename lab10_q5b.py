def circular_shift(lst, k, direction='left'):
    n = len(lst)
    k = k % n
    if direction == 'left':
        return lst[k:] + lst[:k]
    elif direction == 'right':
        return lst[-k:] + lst[:-k]
l = []
x = int(input('enter length of list:'))
for i in range (x):
    e = int(input('enter elements of list:'))
    l.append(e)
k = int(input('enter value of shift'))
print(l)
shifted_left = circular_shift(l, k, 'left')
print("Shifted left:", shifted_left)

shifted_right = circular_shift(l, k, 'right')
print("Shifted right:", shifted_right)
