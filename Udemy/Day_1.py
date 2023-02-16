print("Day 1 - Python print function")
print("The function is declared like this:")
print("print('what to print')\n")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\""+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.\n")

# Input function takes the input from the system and return the value as a string.
# len() function returns the total number of charecters in the string.
a = input("What is your name? ")
print(len(a))
print("\n")

# VARIABLE EXERCISE --------------------------------------
# Write a program that switches the values stored in the variables a and b.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
temp = a
a = b
b = temp



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
print("\n")
# ---------------------------------------------------------

print("Hello " + input())