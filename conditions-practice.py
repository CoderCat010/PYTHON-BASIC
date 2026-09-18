age = 20
if age > 18:
    print('you are an adult')

a = 33
b = 3
if a > b: 
    print('a is greater than b')
elif b > a: 
    print('b is greater than a')

a = 3
b = 3
if a > b: 
    print('a is greater than b')
elif b > a: 
    print('b is greater than a')
else: 
    print('no they are not equal')


# shorthand if else
a = 2
b = 3
print('a is greater than b') if a > b else print('b is greater than a')


# logical operators for conditions
a = 2
b = 3
c = 3
if a < c and b == c: 
    print('both conditions are true')
if a < c or b == c: 
    print('At least one of the conditions is True')