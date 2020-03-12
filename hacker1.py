'''string='abracadabra'
l=list(string)
l[5]='k'
print(l)
string=''.join(l)
print(string)'''

'''string='abracadabra'
string=string[:5]+'k'+ string[6:]
print(string)'''


string='abracadabra'
l=list(string)
print(l)
index=int(input('enter the index'))
for i in l:
    l[index]='k'
string=''.join(l)
print(string)


