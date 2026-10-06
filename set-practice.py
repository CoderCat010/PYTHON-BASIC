# x = {1, 2, 3, 4, 5}
# print(x)

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# x = {1, 2, 3, 4, 5}
# print(len(x))

# x = {1, 2, 3, 4, 5}
# for i in x: 
#     print(i)

# if 6 in x: 
#     print('true')

#----- Methods
# add items
# thisset = {1, 2, 3, 4}
# thisset.add(5)
# print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]
x = thisset.update(tropical)
thisset.update(mylist)
print(thisset)