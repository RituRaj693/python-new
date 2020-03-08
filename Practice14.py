n=input('enter the string :')
count=0
vow='aAeEiIoOuU'
for i in n:
    for j in vow:
        if j==i:
            count=count+1
            print('vowels are',j)
print('no. of vowels are',count)


