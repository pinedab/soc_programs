# Exercise 39 - Dictionaries - Oh, lovely dictionaries
# create a mapping of state to abbreviation
states = {
    'Texas': 'TX',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Pennsylvania': 'PA'
}

# creat a basic set of states and some cities in them
cities = {
    'TX': 'Houston',
    'PA': 'Philadelphia',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['CA'] = 'Los Angeles'

# print some cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("TX State has:", cities['TX'])
# print some states
print('-' * 10)
print("Pennsylvania's abbreviation is:", states['Pennsylvania'])
print("Florida's abbreviation is:", states['Florida'])

# do it by using the state then the cities dict
print('-' * 10)
print("Pennsylvania has:", cities[states['Pennsylvania']])
print("Florida has:", cities[states['Florida']])
# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every sity in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abreviation by state that might not be there
state = states.get("Michigan")
if not state:
    print(f"Sorry, no Michigan")

# get a city with a default value
city = cities.get('MI', 'Does not Exist')
print(f"The city for the state 'MI' is: {city}")
