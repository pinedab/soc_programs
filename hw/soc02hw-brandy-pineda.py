##### Things to Try:

##### DAY1 #####

# 1. Calculate a table for each letter in the alphabet 
# from a-z, and count how many times each letter appears
# in alice_in_wonderland.txt (fancy word for counting
# stuff is "frequency distribution" - because you are 
# counting the frequency of something).
# a: 34,560
# b: 5,027
# ...
# z: 893
# Store the results in a list of lists:
# result = [ ["a", 34560], ["b", 5027], ... , ["z", 893] ]
# Hint: use python's lower() method isalpha() method
def count_letters(filename = "alice_in_wonderland.txt"):
	file = open(filename,"r", encoding ="utf8") 
	raw = file.read()
	result = []
	for a in range(122, 96, -1):
		result.append([chr(a), 0])
		
	for a in range(97, 123):
		for r in raw[:len(raw)]:
			if r.isalpha():
				if chr(a) == r.lower():
					for n in range(25,-1,-1):
						if n == (122 - a):
							result[n][1] += 1
	return print(result)

count_letters()
print()
##### DAY 2 #####
# 2. There is something small that needs fixing. 
# Can you spot it and fix it? (Hint, we only want A-Z and a-z)
def display_abcs():
	for x in range(65,65 + 2 * 26 + 6):
		if 91 > x or x > 96:
			print(x, "stands for", chr(x))
display_abcs()
print()

# 3. Make a function that prints A-Z and a-z
def print_abcs():
	for x in range(65,65 + 2 * 26 + 6):
		if 91 > x or x > 96:
			print(chr(x))

print(print_abcs())
print()
# 4. Make a function that asks the user for a message, 
# and turns it into a list of numbers. (It's a cypher ;))
# "I LOVE YOU" [ 73, , 76, ...]
def cypher(q):
	msg = []
	print(q)
	reply = input('> ')
	if reply:
		for a in reply:
			msg.append(ord(a))
	else:
		print("No message detected. Try again")
		cypher(q)
	return print(msg)

cypher("What's your secret message?")
print()

# 5. Optional: Write a function that does a ceaser cypher 
# (Google), ask the user a number, and shift their message 
# by that number.
def ceasar(q):
	msg = []
	print(q)
	shift = int(input("Pick a number: "))
	reply = input('> ')
	if isinstance(shift, int):
		if reply:
			for a in reply:
				msg.append(ord(a) + shift)
		else:
			print("No message detected. Try again")
			ceasar(q)
	else:
		print("Not a valid number. Try again")
		ceasar(q)
	return print(msg)

ceasar("What's your secret message?")
print()

# 6. Write a function that prints out all elements of the
# below board, starting from the first element of the 
# first line, till the end. Each line should be read 
# from beginning to end.
M = "land"
o = "water"
world = [[o,o,o,o,M,o,o,o,o,o,o],
		 [o,o,o,o,M,M,o,o,o,o,o],
		 [o,o,o,o,o,o,o,o,M,M,o],
		 [o,o,o,M,o,o,o,o,o,M,o],
		 [o,o,o,M,o,M,M,o,o,o,o],
		 [o,o,o,o,M,M,M,M,o,o,o],
		 [o,o,o,M,M,M,M,M,M,M,o],
		 [o,o,o,M,M,o,M,M,M,o,o],
		 [o,o,o,o,o,o,M,M,o,o,o],
		 [o,M,o,o,o,M,o,o,o,o,M],
		 [o,o,o,o,o,o,o,o,o,o,o]]

def read_elements(w = world):
	for i in range(0, len(w)):
		for j in range(0, len(w[i])):
			each = w[i][j]
			print(each)

read_elements()
print()

# 7. Now write a function that prints out all elements 
# in reverse.
def reverse_elements(w = world):
	for i in range(len(w) - 1, -1, -1):
		for j in range(len(w[i]) -1, -1, -1):
			each = w[i][j]
			print(each)

reverse_elements()

# 8. There is one small bug in the continent counter below.
# Can you find it and fix it? (Hint: change the world so
# that the continent borders the edge)
def continent_counter(world, x, y):
	if world [x][y] != 'land':
	# Either it's water or we already counted it,
	# but either way, we don't want to count it now.​
		return 0

	# So first we count this tile...
	size = 1
	world[x][y] = 'counted land'	

	# ...then we count all of the nieghboring eight tiles
	# (and, of course, their neighbors by way of recursion)
	if -1 < y-1 < len(world[x] or -1 < x < len(world)):
		size = size + continent_counter(world, x-1, y-1)
		size = size + continent_counter(world, x , y-1)
		size = size + continent_counter(world, x+1, y-1)
	if -1 < x+1 < len(world[x] or -1 < x-1 < len(world)):	
		size = size + continent_counter(world, x-1, y )
		size = size + continent_counter(world, x+1, y )
	if -1 < y+1 < len(world[x]):
		size = size + continent_counter(world, x-1, y+1)
		size = size + continent_counter(world, x , y+1)
		size = size + continent_counter(world, x+1, y+1)
	return size

print(continent_counter(world, 5, 5)) #23
print(continent_counter(world, 1, 4)) #2
print()

##### DAY 3 #####
# 9. Modify "a" for another name in my_dict. Hint: you will 
# have to create a new key-value pair, copy in the value,
# and then delete the old one.
dict_a = { 'a': "Apple", 'b': "Banana", 'c': "Cantalope" }
print(dict_a['a'])
dict_a['a'] = "Apricot"
print(dict_a['a'])
print()
dict_a['p'] = dict_a['b']
del dict_a['b']
print(dict_a)

# 10. Redo the frequency distribution of 
# alice_in_wonderland.txt and save your result in a dictionary.
def count_letters_dict(filename = "alice_in_wonderland.txt"):
	file = open(filename,"r", encoding ="utf8") 
	raw = file.read()
	result = {}
	for a in range(122, 96, -1):
		result[chr(a)] = 0
		
	for a in range(97, 123):
		for r in raw[:len(raw)]:
			if r.isalpha():
				if chr(a) == r.lower():
					for n in range(25,-1,-1):
						if n == (122 - a):
							result[chr(a)] += 1
	return print(result)

count_letters_dict()
print()
# 11. Create a dictionary with your own personal details,
# feel free to be creative and funny so for example, 
# you could include key-value pairs with quirky fact, 
# fav quote, pet. Practice adding, modifying, accesing.
animals = {'cat': 2, 'dog': 34, 'elephant': 32, 'whale': 23, 'hamster': 15 }
print(animals)
print(f"There are {animals['dog']} dogs.")
del(animals['whale'])
print("There are no more whales.\n", animals)

# 12. Translate the real world 1MWTT student into a Student 
# class, decide on all the attributes that would be meaningful.
class Student():
        # constructor?
    def __init__(self, ask_id, track, dream, location):
        self.id_name = ask_id
        self.track = track
        self.dream = dream
        self.location = location

    def my_print(self):
        print(self.id_name + ' ' + self.track)
print()

# 13. Search online for "object-oriented programming" and 
# try to overflow your brain with what you read. Don't 
# worry if it makes absolutely no sense to you. Half of 
# that stuff makes no sense to me too.
