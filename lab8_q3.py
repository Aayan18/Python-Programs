def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
my_list = []
N = int(input('enter length of list:'))
for i in range (N):
    e = int(input('enter elements of list:'))
    my_list.append(e)
bubble_sort(my_list)

print("Sorted list:", my_list)