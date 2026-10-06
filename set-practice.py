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


# update ---- to concatinate another types of list collection with set
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# mylist = ["kiwi", "orange"]
# x = thisset.update(tropical)
# thisset.update(mylist)
# print(thisset)


# remove, dischard
# thisset = {"apple", "banana", "cherry"}
# thisset.remove('banana')
# thisset.pop('banana')
# thisset.clear()
# thisset.discard('banana')
# print(thisset)


# copy
# thisset = {"apple", "banana", "cherry"}
# x = thisset.copy()
# y = x.add(3)
# print(x)


# union
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A | B)
# print(A.union(B))


# intersection
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A & B)
# print(A.intersection(B))


# difference
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A - B)
# print(A.difference(B))


# symmetrick differance
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A ^ B)
print(A.symmetric_difference(B))