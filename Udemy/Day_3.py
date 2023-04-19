print("Welcome to the rollercoaster ride!!")
height =int(input("What is your height in cm?"))

if height >= 120 :
    print("\nYou can ride the rollercoaster.")
else:
    print("\nBruuuh!!!! Come on grow taller motherfucker.")
    
# ------------------------------------------------------------------------------------
# ----------------------------ODD AND EVEN--------------------------------------------

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# -------------------------------------------------------------------------------------
# ----------------------------Nested If- else / Elif-----------------------------------
print("Welcome to the rollercoaster ride!!")
height =int(input("What is your height in cm?"))

if height >= 120:
    print("\nYou can ride the rollercoaster.")
    age = int(input("What's your age alien?"))
    if age < 12:
        print("Please pay up bitch. $5 it is")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Hello Adult!! I know your life is fucked up so pay abit extra for your drama. $12")
else:
    print("\nBruuuh!!!! Come on grow taller motherfucker.")

# -------------------------------------------------------------------------------------
