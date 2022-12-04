random_numbers=[4,56,75,6,3,2,8,567,45]
friends = ["Arnav", "Bhaba", "Sankalp", "Jay"]

# Add two list together
friends.extend(random_numbers)
print(friends)

# Add element to the list
random_numbers=[4,56,75,6,3,2,8,567,45]
friends = ["Arnav", "Bhaba", "Sankalp", "Jay", "Jay","Jay"]

friends.append("Gloria")
print(friends)

# Insert element at certain index in the list
friends.insert(2,"Nancy")
print(friends)

# Remove elements fro the list
friends.remove("Nancy")
friends.remove("Gloria")
print(friends)

# Delete all elements of the list
random_numbers.clear()
print(random_numbers)

# Pops the last element in the list i.e deletes and return the last element
print(friends.pop(1))
print(friends.pop())

# Spot specific elements inside of the list
print(friends.index("Arnav"))
# print(friends.index("Nancy"))
# If the element is not present inside ofthe list it throws an error.

# Count the number of occurance of an element
print(friends.count("Jay"))

# Sort a lsit
friends.sort()
print(friends)

# Reverse the list
friends.reverse()
print(friends)

# Copy a list to another one.
frnds = friends.copy()
print(frnds)