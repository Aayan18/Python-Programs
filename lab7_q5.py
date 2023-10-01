s = str(input('enter a para:'))
Alpha_lower = 0
Alpha_upper = 0
Digit = 0
Sp_chr = 0
for char in s:
    if char.islower():
        Alpha_lower+= 1
    elif char.isupper():
        Alpha_upper+=1
    elif char.isdigit():
        Digit+=1
    else:
        Sp_chr+=1
print(Alpha_lower)
print(Alpha_upper)
print(Digit)
print(Sp_chr)
