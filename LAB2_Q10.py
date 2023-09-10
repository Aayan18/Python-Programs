tm = int(input('enter num:'))
if 1<=tm<=86400:
    hr = tm//(60*60)
    b = tm%(60*60)
    min = b//60
    sec = b%60
    print (hr,min,sec)
else :
    print ('invalid')
       
    
    