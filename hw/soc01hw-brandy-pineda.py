# ##### Write a program that tells you the following:

# #####DAY1
# # 1. Hours in a year. How many hours are in a year?
# print(24 * 365)

# # 2. Minutes in a decade. How many minutes are in a decade?
# print((60 * 24) *365* 10)

# # 3. Your age in seconds. How many seconds old are you? 
# print(60*60*(24 * 365 * 21))

# # 4. Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
# print(48618000 / (60*60*24*365) * 10)

# #####DAY2 NONE

# #####DAY3
# # 5. Full name greeting. Write a program that asks for a 
# # person’s first name, then middle, and then last. Finally,
# # it should greet the person using their full name.
# first = input("Enter first name: ").lower()
# mid = input("Enter second name: ").lower() + ' '
# last = input("Enter last name: ").lower()
# print("Nice to meet you, " + first.capitalize() + ' ' + mid.capitalize() + last.capitalize())

# # 6. Bigger, better favorite number. Write a program that
# # asks for a person’s favorite number. Have your program 
# # add 1 to the number, and then suggest the result as a 
# # bigger and better favorite number. (Do be tactful 
# # about it, though.)
# fav = input("What's your favorite number?")
# big = int(fav) + 1
# print("A bigger and better number is this: " + str(big))	

# # 7. Angry boss. Write an angry boss program that rudely 
# # asks what you want. Whatever you answer, the angry boss
# # should yell it back to you and then fire you. For example, 
# # if you type in I want a raise, it should yell back like this:
# # WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
# employee = input("What would you like to ask DA BOSS?")
# print("WHAT DO YOU MEAN '" + employee.upper() + "'?! YOU ARE FIRED!!")

# # 8. Table of contents. Here’s something for you to do in 
# # order to play around more with center, ljust, and rjust: 
# # write a program that will display a table of contents 

# c = "Chapter 1: Getting Started"
# cc = " Chapter 2: Numbers"
# ccc = "Chapter 3: Letters"
# p = "page 1"
# pp = "page 9"
# ppp = "page 13" 
# # Printing the original string
# print ("The original string is : \n", c, "\n")
# print ("The original string is : \n", cc, "\n")
# print ("The original string is : \n", ccc, "\n")
 
# # Printing aligned strings
# print ("The right aligned: ")
# print (c + p.rjust(40, '.'))
# print (cc + pp.rjust(40, '.'))
# print (ccc + ppp.rjust(40, '.'))
# print()
# print ("The left aligned: ")
# print (p.ljust(40, '.') + c)
# print (pp.ljust(40, '.') + cc)
# print (ppp.ljust(40, '.') + ccc)
# print()
# print ("The center aligned: ")
# print ((c + ' - ' + p).center(40, '.'))
# print ((cc + ' - ' + pp).center(40, '.'))
# print ((ccc + ' - ' +ppp).center(40, '.'))

# # DAY4
# # 9. “99 Bottles of Beer on the Wall.” Write a program that
# prints out the lyrics to that beloved classic, “99 Bottles
# of Beer on the Wall.”
print()
bottles = input("How many bottles are on the wall? ")
b = 0
while bottles.isalpha():
	bottles = input("How many bottles are on the wall?")
	print("Please type a number")
if not bottles.isalpha() and int(bottles) > 0: 
	b = int(bottles)
for x in range(b, -1, -1):
	if x == 0:
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, " + bottles + " bottles of beer on the wall.")
	elif x == 1:
		print("1 bottle of beer on the wall, 1 bottle of beer.")
		print("Take one down and pass it around, no more bottles of beer on the wall.")
	else:
		print(str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
		print("Take one down and pass it around, " + str(x - 1) + " bottle of beer on the wall.")

# 10a. Deaf grandma. Whatever you say to Grandma (whatever you type
# in), she should respond with this: HUH?! SPEAK UP, GIRL! Unless
# you shout it (type in all capitals). If you shout, she can
# hear you (or at least she thinks so) and yells back: 
# NO, NOT SINCE 1938! To make your program really believable,
# have Grandma shout a different year each time, maybe any 
# year at random between 1930 and 1950. You can’t stop 
# talking to Grandma until you shout BYE.

# 10b. Deaf grandma extended. What if Grandma doesn’t want 
# you to leave? When you shout BYE, she could pretend not to
# hear you. Change your previous program so that you have to 
# shout BYE three times in a row. Make sure to test your 
# program: if you shout BYE three times but not in a row, 
# you should still be talking to Grandma.

# 11. Leap years. Write a program that asks for a starting 
# year and an ending year and then puts all the leap years
# between them (and including them, if they are also leap
# years). Leap years are years divisible by 4 (like 1984 
# and 2004). However, years divisible by 100 are not leap
# years (such as 1800 and 1900) unless they are also 
# divisible by 400 (such as 1600 and 2000, which were 
# in fact leap years). What a mess!

# 12. Find something today in your life, that is a 
# calculation. Go for a walk, look around the park, try 
# to count something. Anything! And write a program about
# it. e.g. number of stairs, steps, windows, leaves 
# estimated in the park, kids, dogs, estimate your books
# by bookshelf, toiletries, wardrobe.
