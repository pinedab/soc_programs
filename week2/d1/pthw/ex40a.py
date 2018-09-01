# Exercise 40 - Modules, Classes, and Objects
# instantiate/Create a class == a object (of that class)

# Three Ways of accessing things

# dictionary style
# Sample
mystuff1 = {'apple': "I AM APPLES!"}
print(mystuff1['apple'])

# module style
# Sample - mystuff.py exists w code inside
import mystuff
mystuff.apple()
print(mystuff.tangerine)

# class style


class MyStuff(object):

    def __init__(self):
        self.nectarine = "And I - Will - Al - Ways Lah-uh-vee Youu!"

    def oranges(self):
        print("I AM FOXY ORANGES")


thing = MyStuff()  # instantiate here
thing.oranges()
print(thing.nectarine)
