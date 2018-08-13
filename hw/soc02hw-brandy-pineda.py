# ##### Things to Try:

# ##### DAY1 #####

# # 1. Calculate a table for each letter in the alphabet 
# # from a-z, and count how many times each letter appears
# # in alice_in_wonderland.txt (fancy word for counting
# # stuff is "frequency distribution" - because you are 
# # counting the frequency of something).
# # a: 34,560
# # b: 5,027
# # ...
# # z: 893
# # Store the results in a list of lists:
# # result = [ ["a", 34560], ["b", 5027], ... , ["z", 893] ]
# # Hint: use python's lower() method isalpha() method
# def count_letters(filename = "alice_in_wonderland.txt"):
# 	file = open(filename,"r", encoding ="utf8") 
# 	raw = file.read()
# 	result = []
# 	for a in range(122, 96, -1):
# 		result.append([chr(a), 0])
		
# 	for a in range(97, 123):
# 		for r in raw[:len(raw)]:
# 			if r.isalpha():
# 				if chr(a) == r.lower():
# 					for n in range(25,-1,-1):
# 						if n == (122 - a):
# 							result[n][1] += 1
# 	return print(result)

# count_letters()
# print()
# ##### DAY 2 #####
# # 2. There is something small that needs fixing. 
# # Can you spot it and fix it? (Hint, we only want A-Z and a-z)
# def display_abcs():
# 	for x in range(65,65 + 2 * 26 + 6):
# 		if 91 > x or x > 96:
# 			print(x, "stands for", chr(x))
# display_abcs()
# print()

# # 3. Make a function that prints A-Z and a-z
# def print_abcs():
# 	for x in range(65,65 + 2 * 26 + 6):
# 		if 91 > x or x > 96:
# 			print(chr(x))

# print(print_abcs())
# print()
# # 4. Make a function that asks the user for a message, 
# # and turns it into a list of numbers. (It's a cypher ;))
# # "I LOVE YOU" [ 73, , 76, ...]
# def cypher(q):
# 	msg = []
# 	print(q)
# 	reply = input('> ')
# 	if reply:
# 		for a in reply:
# 			msg.append(ord(a))
# 	else:
# 		print("No message detected. Try again")
# 		cypher(q)
# 	return print(msg)

# cypher("What's your secret message?")
# print()

# # 5. Optional: Write a function that does a ceaser cypher 
# # (Google), ask the user a number, and shift their message 
# # by that number.
# def ceasar(q):
# 	msg = []
# 	print(q)
# 	shift = int(input("Pick a number: "))
# 	reply = input('> ')
# 	if isinstance(shift, int):
# 		if reply:
# 			for a in reply:
# 				msg.append(ord(a) + shift)
# 		else:
# 			print("No message detected. Try again")
# 			ceasar(q)
# 	else:
# 		print("Not a valid number. Try again")
# 		ceasar(q)
# 	return print(msg)

# ceasar("What's your secret message?")
# print()

# 6. Write a function that prints out all elements of the
# below board, starting from the first element of the 
# first line, till the end. Each line should be read 
# from beginning to end.
M = "land"
o = "water"
world = [[o,o,o,o,o,o,o,o,o,o,o],
		 [o,o,o,o,M,M,o,o,o,o,o],
		 [o,o,o,o,o,o,o,o,M,M,o],
		 [o,o,o,M,o,o,o,o,o,M,o],
		 [o,o,o,M,o,M,M,o,o,o,o],
		 [o,o,o,o,M,M,M,M,o,o,o],
		 [o,o,o,M,M,M,M,M,M,M,o],
		 [o,o,o,M,M,o,M,M,M,o,o],
		 [o,o,o,o,o,o,M,M,o,o,o],
		 [o,M,o,o,o,M,o,o,o,o,o],
		 [o,o,o,o,o,o,o,o,o,o,o]]

# def read_elements(w = world):
# 	for i in range(0, len(w)):
# 		for j in range(0, len(w[i])):
# 			each = w[i][j]
# 			print(each)

# read_elements()
# print()
# 7. Now write a function that prints out all elements 
# in reverse.
def reverse_elements(w = world):
	for i in range(len(w) - 1, -1, -1):
		for j in range(len(w[i]) -1, -1, -1):
			each = w[i][j]
			print(each)

reverse_elements()
# 8. There is one small bug in the continent counter above.
# Can you find it and fix it? (Hint: change the world so
# that the continent borders the edge)

# 9. Write a function that generates an n x n sized board 
# with either land or water chosen randomly.

# Optional, Advanced
# 10. Run your continent counter for a 20 x 20 board. How 
# long does it take to run? (If it runs quickly, try 
# 30 x 30 ... 100 x 100 just be aware you might end up 
# in a VERY LOOOONG WAIT) - make sure you know how to 
# break a running program as it may take a long time to 
# complete and you might not have time to wait for it ;)

# 11. Write test coverage in unittest and/or trace for 
# Continent Counter

##### DAY 3 #####