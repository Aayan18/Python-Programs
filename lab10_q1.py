para=input("Enter a paragraph: ").lower()
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in para:
    if i in 'aeiou':
        vowels[i]+=1
sort=dict(sorted(vowels.items()))
print("count of vowels:")
for vowel, count in sort.items():
    print(vowel,":",count)


