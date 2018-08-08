## SOC Week 2 Day 1

## Functions, parameters
def woof(n):
	# print('woof ' * n)
	return 'woof ' * n

def ask_recursively(q):
	print(q)
	reply = input('> ').lower()
	if reply == 'yes':
		return True
	if reply == 'no':
		return False
	else:
		print("Please answer 'yes' or 'no'.")
		ask_recursively(q)

ask_recursively('Do you like Mexican food?')

## Testing
# manual testing
# for x in range(3):
# 	woof(x)
# 
# vs
# unit testing
# uses test_<filename> as a new file
# w appropiate imports


# Reading and Writing Files
filename = "alice_in_wonderland.txt"
file = open(filename,"r", encoding ="utf8") # loads it in to our program
# for line in file:
# OPENS FILE SEQUENTIALLY, NOTHING LEFT TO READ AFTER print()
# 	print(line)

raw = file.read()
print(raw[:65]) # reads char 0 until char 65
print(f"The length of this book is {len(raw)} characters!")
# COUNTING == FREQUENCY DISTRIBUTION