age = 20
if age < 30:
    print("age is less than 30")

if age == 20:
    print("age is 20")

if age != 30:
    print("age is not 30")

if age & age < 30:
    print("age is not null and less than 30")

if age > 10 | age < 30:
    print("age between 10 and 30")

if age > 30:
    print("age greater than 30")
elif age < 10:
    print("age less than 10")
else:
    print("this")

x = 1
y = 30
if 2 < x <= 10:
    print("x between two and ten")
if x > 2 or x <= 20:
    print("x is gt 2 or lt 20")
if not (x == y):
    print("x is not equals y")
