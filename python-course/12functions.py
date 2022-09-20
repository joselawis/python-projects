def hello(name):
    print(f"HELLO {name}")


def add(number_one, number_two):
    return number_one + number_two


add_lambda = lambda number_one, number_two: number_one + number_two

hello("IlloJuan")
print(add(1, 2))

print(add_lambda(10, 30))
