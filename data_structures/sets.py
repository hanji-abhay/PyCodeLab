# Sets in Python
# Sets are unordered collections of unique elements
# They are changeable, but do not allow duplicates
# Syntax: my_set = {1, 2, 3}

# Creating a set
numbers = {1, 2, 3, 4, 4, 5}  # duplicate 4 is automatically removed
print("Initial set:", numbers)
print("Type of numbers:", type(numbers))

# 1. Adding elements
numbers.add(6)  # Adds 6 to the set
print("After adding 6:", numbers)

# 2. Removing elements
numbers.remove(2)  # Removes 2 from set
print("After removing 2:", numbers)

# 3. Discarding an element
numbers.discard(10)  # Removes 10 if exists; does nothing if not
print("After discard 10:", numbers)

# 4. Popping an element (removes arbitrary item)
popped = numbers.pop()
print("Popped element:", popped)
print("Set after pop:", numbers)

# 5. Clearing the set
temp_set = numbers.copy()  # copying to demonstrate clear
temp_set.clear()
print("Cleared set:", temp_set)

# Looping through a set
print("Looping through set:")
for num in numbers:
    print(num)

# Set operations with another set
evens = {2, 4, 6, 8}
print("Another set (evens):", evens)

# Union
union_set = numbers | evens
print("Union:", union_set)

# Intersection
intersection_set = numbers & evens
print("Intersection:", intersection_set)

# Difference
difference_set = numbers - evens
print("Difference:", difference_set)

# Symmetric Difference
sym_diff_set = numbers ^ evens
print("Symmetric Difference:", sym_diff_set)

# Checking membership with if-else
check_num = int(input("Enter number to check in the set: "))
if check_num in numbers:
    print(f"{check_num} exists in the set")
else:
    print(f"{check_num} does not exist in the set")
