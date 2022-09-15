colors = ["red", "green", "blue"]

fibonacci = list((1, 1, 2, 3, 5, 8))
print(fibonacci)

range_list = list(range(1, 100))
print(range_list)

print(dir(colors))

print(len(colors))

print("green" in colors)
colors[1] = "yellow"
print(colors)

# colors.append(('violet', 'green')) # add a tuple as a new element
colors.extend(("violet", "green"))  # add the two new values as two new elements
print(colors)

colors.insert(len(colors), "black")
print(colors)

colors.pop()
print(colors)

colors.pop(1)
print(colors)

colors.remove("violet")
print(colors)

colors.sort(reverse=True)
print(colors)

print(colors.index("red"))

print(colors.count("red"))
