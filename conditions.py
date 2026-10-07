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

a = 2
b = 5
if not a > 5: 
    print('a is not greater than b')


age = 25
is_student = False
has_discount_code = True
if (age > 18 or age < 60) and not is_student or has_discount_code: 
    print('Discount applies!')


'''
Problem 1:
input:
একটা ব্যক্তির বয়স (age) input হিসেবে দেওয়া থাকবে। তুমি প্রোগ্রাম লিখবে যেটা বলবে সে কোন category-তে পড়ে:

output: 
- বয়স 0-12 হলে → "Child"
- বয়স 13-19 হলে → "Teenager"
- বয়স 20-59 হলে → "Adult"
- বয়স 60 বা তার বেশি হলে → "Senior"
'''
enterYourAge = int(input())
if (enterYourAge >= 0 and enterYourAge <= 12):
    print(enterYourAge, 'child')
elif (enterYourAge >= 13 and enterYourAge <= 19):
    print(enterYourAge, 'teenager')
elif (enterYourAge >= 20 and enterYourAge <= 59):
    print(enterYourAge, 'adult')
else: 
    print(enterYourAge, 'old')