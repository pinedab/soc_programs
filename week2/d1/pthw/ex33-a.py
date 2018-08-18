# Exercise 33 - Rewritten as a function
def number_list(i=0, max=6, inc=1):
    print("Let's make a lst of numbers!")
    print("Where do you want the list of numbers to start?")
    i = int(input("> "))
    nums = []

    print("Where do you want the list of numbers to end?")
    max = int(input("> ")) + 1

    print("By how much would you like to increment?")
    inc = int(input("> "))

    while i < max:
        print(f"At the top i is {i}")
        nums.append(i)

        i += inc

        print("Nums now:", nums)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for n in nums:
        print(n)


number_list()
