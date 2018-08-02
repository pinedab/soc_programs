##### LOOPS #####

## WHILE ##
i = 1
while i < 6:
	print(i)
	i = i + 1 #crucial to include
print('____\n')
j = 0
while j < 11:
	print(j) #print HERE to show last count
	if j == 3:
		break # stops at j = 3
		# print(j) #print HERE NOT to show last count
	j += 1
print('____\n')

## FOR ## for x in range(10): #range(start, end noninclusive,
increment)     print(x) # 0 1 2 3 4 5 6 7 8 9 print('____\n')  dogs =
["Bean Fouler", "Chewy Pena",  "Grizz Bearington", "Nina Pineda"]
skill = ["napper", "jumper", "barker", "cuddler"] c = 0 for s in dogs:
print(s + " is an amazing " + skill[c] + "!")     c += 1
print('____\n')


## if elif else ##
# NO SWITCH CASE IN PYTHON