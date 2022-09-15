colors = {"red", "green", "blue"}

print(colors)
print(type(colors))
print(dir(colors))

print("red" in colors)
colors.add("violet")
print(colors)
colors.add("violet")
print(colors)

colors.remove("violet")
print(colors)

del colors
