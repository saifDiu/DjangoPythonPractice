
letter = ['a','b','c','d']
print('Before reassignment:')
print(letter)
letter[0] = 'G'
print('After reassignment:')
print(letter)
list = ['a',1,3,4,['d','e']]
print(list)
list.append("new item")
print(list)
flist = ['a','b','c','d']
print(flist)
print('After extend:')
flist.extend(['e','f','g'])
print(flist)

#popUp method

list = [1,2,3,4,5]
item = list.pop()
sitem = list.pop(0)
print(list)
print(item)
print("After pop by index 0: ")
print(list)
print(sitem)

#sort
list = [3,5,12,4,56,7,8,9,34]
list.sort()
print(list)
list.reverse()
print(list)
