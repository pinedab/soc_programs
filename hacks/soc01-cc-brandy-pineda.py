import random

def grid(row = 11, col = 11, chars = "XO"):
	g = ''
	for x in range(row):
		g += ((''.join(random.choice(chars) for x in range(col))) + '\n')
	return g

def continent_count():
	a = grid()
	b = len(a)
	c = 0
	land = 0

	for x in a:
		if x == 'X':
			land += 1
			c = c + 1
		elif x == 'O': 
			c = c + 1	
		else: 
			pass

	return "Land: " + str(land) + "\nWater: " + str(b - land) + "\nTotal: " + str(b) + "\n" + a

print(continent_count())