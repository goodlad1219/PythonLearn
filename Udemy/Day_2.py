a = 123_456_789
print(a)
print(type(a))

# '_'under scores are just to make it human readable. computers do not takes it into consideration.

# EXERCISE 1 ------------------------------------------------------------
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# num = (int)(two_digit_number)
# sum = 0
# sum = (int)((num/10) + (num%10))
# '/' operator returns float value. Hence We had to type cast again.
# print(sum)

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)

# -----------------------------------------------------------------------