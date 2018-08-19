# SOC Week 2 Day 3

# WAY 1 TO INSTANTIATE A DICT
my_dict = {'a': 35000,
           'b': 7000,
           'z': 450}

# print(my_dict)

# access
my_dict['b']

# add
my_dict['c'] = 3245

# modify - overwriting
my_dict['a'] = 35550
# print(my_dict)

# del item
del(my_dict['a'])
print(my_dict)

# del dictionary
del(my_dict)

# WAY 2 TO INSTANTIATE A DICT
# Dictionary constructor 
brandy = dict(name = "yeleine", id = "4367", fav_food = "ice cream")
print(brandy)