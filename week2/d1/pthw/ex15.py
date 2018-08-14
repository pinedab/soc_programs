# Exercise 15
from sys import argv
# takes in arguments from cmd
script, filename = argv
# saves argument
txt = open(filename)

print(f"Here's your file {filename}:")
# reads/prints the saved file
print(txt.read())
# saves file in another var. accesses and reads tha second var
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
