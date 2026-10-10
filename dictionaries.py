thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict["brand"])
# print(len(thisdict))
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())


# loop through dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])


# methods
# d[key]
# marks = {"Rahim": 80, "Karim": 65}
# print(marks['Rahim'])
# print(marks.get('ehim'))
# print(marks.get('ehim', 'no value found!'))


# d[value] change & add
# marks = {"Rahim": 80, "Karim": 65}
# marks['Karim'] = 40
# marks["Sumi"] = 90    
# print(marks)
# print('Karim' in marks)


# pop & del
'''
  - pop ---> remove items & return the removed items
  - popitem ---> remove last items
  - del ---> remove items but return nothing 
'''
# marks = {"Rahim": 80, "Karim": 65}
# removeItems = marks.pop('Rahim')
# removeItems = marks.popitem()
# remove1Items = marks.pop('Rahi', 'value pawa jai ni')

# del marks['Karim']
# print(marks)
# print(removeItems)
# print(remove1Items)


# update ---> add items
# marks = {"Rahim": 80, "Karim": 65}
# marks.update({'color': 'red'})
# print(marks)
