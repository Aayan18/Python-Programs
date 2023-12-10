def sum_of_positive_integers_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_positive_integers_recursive(n-1)
n = int(input('enter a number:'))
result = sum_of_positive_integers_recursive(n)
print(f"The sum of the first {n} positive integers is: {result}")