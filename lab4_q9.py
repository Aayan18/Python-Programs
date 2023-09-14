sen = input('enter the sentence')
up=0
low=0
num=0
spe=0
i=1
l=len(sen)
while i<l:
    char=sen[i]
    if 'A'<=char<='Z':
        up=up+1
    elif "a"<=char<='z':
        low = low+1
    elif '0'<=char<='9':
        num=num+1
    else:
        spe = spe+1
    i= i+1
print(up)
print(low)
print(num)
print(spe)