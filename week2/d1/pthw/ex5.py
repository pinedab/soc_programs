###### Learn Python the Hard Way #####
###### #1mwtt sprinkles #####

# Exercise 5
name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Study Drills
print()
kg = weight * (1 / 2.2036226218)
print(f"{weight} Pounds = {kg} Kilograms")

print("Inches to Centimeters: 74 =>", 2.5 * height)


