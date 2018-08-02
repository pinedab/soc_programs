##### Write a program that tells you the following:

#####DAY1
# 1. Hours in a year. How many hours are in a year?
print(24 * 365)

# 2. Minutes in a decade. How many minutes are in a decade?
print((60 * 24) *365* 10)

# 3. Your age in seconds. How many seconds old are you? 
print(60*60*(24 * 365 * 21))

# 4. Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
print(48618000 / (60*60*24*365) * 10)

#####DAY2 NONE

#####DAY3
# 5. Full name greeting. Write a program that asks for a 
# person’s first name, then middle, and then last. Finally,
# it should greet the person using their full name.
first = input("Enter first name: ").lower()
mid = input("Enter second name: ").lower() + ' '
last = input("Enter last name: ").lower()
print("Nice to meet you, " + first.capitalize() + ' ' + mid.capitalize() + last.capitalize())

# 6. Bigger, better favorite number. Write a program that
# asks for a person’s favorite number. Have your program 
# add 1 to the number, and then suggest the result as a 
# bigger and better favorite number. (Do be tactful 
# about it, though.)
fav = input("What's your favorite number?")
big = int(fav) + 1
print("A bigger and better number is this: " + str(big))	

# 7. Angry boss. Write an angry boss program that rudely 
# asks what you want. Whatever you answer, the angry boss
# should yell it back to you and then fire you. For example, 
# if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
employee = input("What would you like to ask DA BOSS?")
print("WHAT DO YOU MEAN '" + employee.upper() + "'?! YOU ARE FIRED!!")

# 8. Table of contents. Here’s something for you to do in 
# order to play around more with center, ljust, and rjust: 
# write a program that will display a table of contents so 
# that it looks like this:
# Table of Contents
# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

c = "Chapter 1: Getting Started"
cc = " Chapter 2: Numbers"
ccc = "Chapter 3: Letters"
p = "page 1"
pp = "page 9"
ppp = "page 13" 
# Printing the original string
print ("The original string is : \n", c, "\n")
print ("The original string is : \n", cc, "\n")
print ("The original string is : \n", ccc, "\n")
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned: ")
print (c + p.rjust(40, '.'))
print (cc + pp.rjust(40, '.'))
print (ccc + ppp.rjust(40, '.'))
print()
print ("The left aligned: ")
print (p.ljust(40, '.') + c)
print (pp.ljust(40, '.') + cc)
print (ppp.ljust(40, '.') + ccc)
print()
print ("The center aligned: ")
print ((c + ' - ' + p).center(40, '.'))
print ((cc + ' - ' + pp).center(40, '.'))
print ((ccc + ' - ' +ppp).center(40, '.'))