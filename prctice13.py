'''def rev(s):
    str=''
    for i in s:
        str=i+str
    return str
s='rituraj'
print(rev(s))'''

#####Method 2 reverse of string
def rev(s):
    if len(s)==0:
        return s
    else:
        return rev(s[1:0])+s[0]
s='rajsi'
print(rev(s))

