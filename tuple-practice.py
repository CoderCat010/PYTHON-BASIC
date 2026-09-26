t = (1, 2, 3)
print(t)
print(t.count(1))
print(t.index(3))

t1 = (1, 2, 3, 4, 5)
t3 = list(t1)
t3[1] = 'kiwi'
t1 = tuple(t3)
print(t3)
print(t1)
