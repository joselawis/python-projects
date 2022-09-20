foods = ["cheese", "milk", "bread", "fruit"]

for food in foods:
    if food == "bread":
        print(f"You must buy this: {food}")
        continue
    print(food)

for number in range(1, 8):
    print(number)

for letter in "Hello":
    print(letter)

count = 4
while count <= 10:
    print(count)
    count += 1
