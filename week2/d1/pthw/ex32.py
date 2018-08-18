# Exercise 32 - Loops and lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of foor-loop goes through a list
for n in the_count:
    print(f"This is count {n}")

# same as above
for f in fruits:
    print(f"A fruit of type: {f}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start e an empty one
elements = []

# then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print(f"Adding {i} to the list.")
#     # append is a function that lists understand
#     elements.append(i)
elements.append(range(0, 6))
# now we can print them out
for i in elements:
    print(f"Element was:", list(i))
