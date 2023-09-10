n = int(input('enter a five digit num:'))
x = n
reverse = 0
while(n>0):
    dig=n%10
    reverse=reverse*10+dig
    n=n//10
if (x==reverse):
    print ('number is palendrom')
else:
    print('number is not palendrom')
            