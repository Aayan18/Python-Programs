s = str(input('enter a sentence:'))
w = str(input('enter a word:'))
s=s.split()
l = len(s)
x=0
for i in range (0,l):
    if w in s[i]:
        x+=1
print(x)        