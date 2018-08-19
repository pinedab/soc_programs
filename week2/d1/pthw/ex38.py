# Exercise 38 - Doing things to lists
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in my list! Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee',
              'Corn', 'Banana', 'Boy', 'Girl']
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")


print(f"\nThere we go:\n{stuff}")

print("\nLet's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
