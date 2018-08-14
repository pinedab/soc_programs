# Exercise 22 -  Study Drills - REVIEW
print() # prints stuff to console
+ # add or concatanate
- # subtract or a negative number
* # multipy numbers, also repeats strings by multiplying
/ # divide, returns float
// # divide, returns int
% # modulos, returns remainder
< # less than
> # greater than
<= # less than or equal
>= # greater than or equal
"..." # double quotes, string
'...' # single quotes, string
a = """ ... """ # triple quotes in a vars, string
""" ... """ # solo triple quotes, comment
print('Dun Dun Dun', a) # comma adds to string w/ a space
print('Dun Dun Dun', a, end='') # end='' adds no new line
= # assignment to a vars
snake_notation = 0 # underscore notation
print(f"I have {snake_notation} cats") #formating a string w vars f >> {}
a = '{} {}'
a.format(True, "love") # .format method, inserts info into {} in a string
esc = 'escape notation isn\'t not cool' # (ex10 full list)use \ to escape ',', '\', '\n', '\t'
b = input("Prompts and saves data from user") #takes info
from sys import argv # takes arguments from cmd line
script, first, second = argv #requires and saves a certain amount of args

#reading and writing file commands
a = "sample.txt"
open(a) # accesses it
a.read() #prints it out
a.truncate() #empties it
a.write("stuff") #adds to it
a.seek(0)#rewinds to beginning
a.readline() # reads until reaches a \n
a.close()#closes it

from os.path import exists 
a = 123 # assignment
len(a) # gives length
exists(a) #returns boolean

def sample(a = 456): # def starts a func, initiate name and args
	print("a = ", a) # function code
	return a    	 # returns a to be used in another func/var if called

