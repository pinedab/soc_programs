# Exercise 21
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDING {a} // {b}")
	return a // b


print("Let's do some math with just functions!")

age = add(14, 8)
height = subtract(78, 10)
weight = multiply(84, 2)
iq = divide(242, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "\n\nCan you do it by hand?")
# Study Drills

print("age + (height - (weight * (iq // 2))) =", age + (height - (weight * (iq // 2))))
