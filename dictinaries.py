#dictionaries

myStuff = {'key1':'saif','key2':'171-35-1926'}
print(myStuff['key2'])
myStudent = {'class1':'Fahim','class2':{'SectionA':['Emon','Prince','Jahid']}}

#LetsFind out Jahid from the dictionaries
print(myStudent['class2']['SectionA'][1])
#reassignment
myStudent['class2']['SectionA'].append('Dosh')
print(myStudent)
print(myStudent['class2']['SectionA'][3])
print(myStudent['class2']['SectionA'][3].upper())
#Add a key into the dictionary
myStudent['class4'] = 'Ashik','Jehad'
print(myStudent)
myStudent['class2'][0] = 'Najmul'
print(myStudent)
