# Exercise 33 - While Loops
i = 0
nums = []

while i < 6:
    print(f"At the top i is {i}")
    nums.append(i)

    i += 1

    print("Nums now:", nums)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for n in nums:
    print(n)
