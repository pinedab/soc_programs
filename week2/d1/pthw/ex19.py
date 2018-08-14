# Exercise 19
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!\nGet a blanket!\n")


print("We can just give the funtction numbers directly:")
cheese_and_crackers(20, 30)


print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study Drills
# Call the function 10 different times
cheese_and_crackers(amount_of_cheese, amount_of_cheese)
cheese_and_crackers(amount_of_crackers, amount_of_crackers)
cheese_and_crackers(amount_of_cheese ** amount_of_crackers,
                    amount_of_crackers ** amount_of_cheese)
cheese_and_crackers(5, 5)
cheese_and_crackers(2 * 5, 10 / 2)
cheese_and_crackers(10 // 2, 100 % 7)
cheese_and_crackers(31465, 243586)
cheese_and_crackers(amount_of_crackers // amount_of_cheese,
                    amount_of_cheese % amount_of_crackers)
cheese_and_crackers(amount_of_crackers - amount_of_cheese,
                    amount_of_crackers * amount_of_cheese)
cheese_and_crackers(cheese_and_crackers(2, 5), cheese_and_crackers(0, 6))
