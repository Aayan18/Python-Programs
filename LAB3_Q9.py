bs = int(input('enter num:'))
hra = 2*bs/10
ta = 5*bs/100
da = bs/10
gs = bs + hra + ta + da
if gs<300000 :
    it = 0
    print(it)
elif 300000<=gs<1000000:
    it = gs/10
    print (it)
elif 1000000<=gs<2500000:
    it = gs*2/10 
    print (it)         
elif gs>=2500000:
    it = gs*0.3
    print (it)
    