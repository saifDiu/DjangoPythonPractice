#Basics
#Two ways of declaration
'My name is saif'
"i'm a student"
#Indexing
country = 'Bangladesh'
#Slicing in python
print(country[-3])
print(country[2:9])
print(country[1:7])
print(country[1::3])
print(country[::3])

#Basic methods in python
name = 'saif'
x = name.upper();
y = name.capitalize();
enc = name.encode();
spl = name.split('a')
print(x)
print(y)
print(enc)
print(spl)

#print formatting in python
x = "my name is: {}".format("saif")
print(x)
x = "my name is: {} and my id is: {}".format("saif","171-35-1926")
print(x)
x = "my id is: {y} and my name is: {x}".format(x="saif", y="171-35-1926")
print(x)
