a = [1, 1, 1, 1, 0,
	 1, 1, 1, 0, 0,
	 1, 0, 0, 0]
b = 15
c = 0

if len(a) < b:
	for x in a:
		if x == 0:
				pass
		else: 
			c = c + 1
else: 
	print("No land")

print(c)