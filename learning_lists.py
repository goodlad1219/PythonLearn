# Creating a list
friends = ["Arnav", "Bhaba", "Sankalp", "Jay"]

# Accesing individual Elements
"""
In case of posetive indexing, indexing starts from 0.
In case of negative indexing it starts from -1, from the other end.
"""
print(friends[0])
print(friends[-4])
friends[0] = "Maira"
print(friends[0])

# Slicing of the list
# <list_name>[<inclusive_index> : <exclusive_index>]

print(friends[1:])
print(friends[:2])
print(friends[-4:])
print(friends[:-1])
print(friends[:])

