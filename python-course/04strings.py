my_str = "Hello World"

# dir() para ver que metodos se pueden aplicar
# print(*dir(my_str), sep="\n")

print(my_str.upper())
print(my_str.swapcase())
print(my_str.capitalize())
print(my_str.replace("Hello", "Bye"))
print(my_str.count("l"))
print(my_str.startswith("Hola"))
print(my_str.split("o"))
print(my_str.find("o"))
print(len(my_str))
print(my_str.index("ll"))
print(my_str.isnumeric())
print(my_str.isalnum())
print(my_str.isalpha())
print(my_str[4])
print(my_str[-1])
print("My name is " + my_str)
print(f"My name is {my_str}")
