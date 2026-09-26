# x = ['x', 'y', 6, 1.5, -8]
# print(x)

# # methods
# x = [1, 2, 3, 4]
# x.append(5)
# print(x)

# # insert ---- to add items
# a = [1, 2, 3, 5]
# a.insert(3,'4')
# a.insert(10,'4')
# a.insert(-10,'4')
# print(a)

# # pop method --- to remove item from the last
# fruits = ["apple", "banana", "mango"]
# removeElm = fruits.pop()
# print(removeElm)
# print(fruits)
# print(fruits.pop(1))
# print(fruits)

# # remove method --- remove item's by their names instead of index
# x = ['a', 'hh', 'jj']
# if 'a'in x:
#     x.remove('a')
#     print(x)

# length 
# x = ['a', 'hh', 'jj']
# print(len(x))

# sort() & sorted()
# x = [2, 5, 1, 4, 3]
# x.sort()
# print(x)

# x = [2, 5, 1, 4, 3]
# print(sorted(x, reverse=True))

x = ['dwdwdede', 'kk', 'dcdd', 'dfdfdvd']
print(sorted(x, key=len))
