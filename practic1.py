
n=int(input('enter the size of list:'))
list1=[]
for i in range(0,n):
    elem=int(input('enter the element :'))
    list1.append(elem)
print('new list',list1)
list1.sort()
print('sorted list',list1)
print('second largest number',list1[-2])

        









