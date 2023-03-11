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

input = len(input("Call me GHOST\n"))
input_str = str(input)
print("GhOsT haaaas " + input_str +" letters. HI haaaaa HAAAAAA")
# ------------------------------------------------------------------------

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = int(weight) / float(height)**2
print(int(BMI))

# -------------------------------------------------------------------------
# ----------------------- F-String In Python ------------------------------

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90-int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

# (f"........{...}.....")
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
# -------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------TIP CALCULATOR--------------------------------------------------------------------------------

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
# 150 * 0.12 + 150 = (150(1+0.12))/5

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
Bill_amount = float(input("What was the total bill? $"))
Tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
Number_of_people = int(input("How many people to split the bill?"))
Amount_per_person = (Bill_amount / Number_of_people) * (Tip_percentage / 100 + 1)
Payable_amount = round(Amount_per_person,2)
print(f"Each person should pay: ${Payable_amount}")


