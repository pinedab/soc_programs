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

##### DAY 2 #####
# 2. There is something small that needs fixing. 
# Can you spot it and fix it? (Hint, we only want A-Z and a-z)
for x in range(65,65 + 2 * 26 + 6):
	print(x, "stands for", chr(x))
# 3. Make a function that prints A-Z and a-z

# 4. Make a function that asks the user for a message, 
# and turns it into a list of numbers. (It's a cypher ;))
# "I LOVE YOU" [ 73, , 76, ...]

# 5. Optional: Write a function that does a ceaser cypher 
# (Google), ask the user a number, and shift their message 
# by that number.

# 6. Write a function that prints out all elements of the
# above board, starting from the first element of the 
# first line, till the end. Each line should be read 
# from beginning to end.

# 7. Now write a function that prints out all elements 
# in reverse.

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