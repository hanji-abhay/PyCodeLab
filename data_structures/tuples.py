# Tuples in Python
# Tuples are ordered, immutable (cannot be changed), allows duplicates

# Creating a tuple
colors = ("red", "green", "blue", "red")
print("Tuple:", colors)
print("Type:", type(colors))

# Accessing elements
print("First color:", colors[0])
print("Slice of tuple:", colors[1:3])

# Looping through tuple
for color in colors:
    print("Color:", color)

# Using tuple with if-else
search_color = input("Enter color to search in tuple: ")
if search_color in colors:
    print(f"{search_color} exists in tuple")
else:
    print(f"{search_color} does not exist in tuple")
