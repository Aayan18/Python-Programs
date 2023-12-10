def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def div(x, y):
    if y != 0:
        return x / y
    else:
        print("Error")
        return None
def mod(x, y):
    if y != 0:
        return x % y
    else:
        print("Error")
        return None
def expo(x, y):
    return x ** y
while True:
    print('add/sub/multiply/divide/remainder/expo/quit')

    operation = input('Enter Operation you want to perform:')

    if operation == 'quit':
        break
    try:
        N1 = float(input('Enter first number:'))
        N2 = float(input('Enter second number:'))
    except ValueError:
        print('Invalid Input')
        continue

    if operation == 'add':
        result = add(N1 ,N2)
    elif operation == 'sub':
         result = subtract(N1, N2)
    elif operation == 'multiply':
        result = multiply(N1, N2)
    elif operation == 'divide':
        result = div(N1, N2)
    elif operation == 'remainder':
        result = mod(N1, N2)
    elif operation == 'expo':
        result = expo(N1, N2)
    else:
        print('Invalid Input')
    print(result)
print ('Thank You')
