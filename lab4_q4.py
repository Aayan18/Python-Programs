num= int(input('enter num:'))
ch = 'yes'
count1 = 0
count2=0
while ch=='yes':
    N=int(input('enter number:'))
    if N%num==0:
        count1+=1
    else:
        count2+=1
    ch=input('do you want to continue(yes,-999)' )
print (count1)
print (count2)






