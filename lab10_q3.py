odd_dict={}
even_dict={}
while True:
        x = input("Enter a number (type 'over' to stop): ")
        if x.lower() == 'over':
            break
        try:
            num= int(x)
            sq = num**2
            cb = num**3
            if num%2==0:
                if num not in even_dict:
                    even_dict[num]=[sq,cb]
            else:
                if num not in odd_dict:    
                    odd_dict[num]=[sq,cb]
        except ValueError:
            print('invalid input')
print(even_dict)
print(odd_dict)