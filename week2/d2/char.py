##### WEEK 2 DAY 2 #####

## Integer into a letter - chr() method ##
for x in range(65,65 + 2 * 26 + 6):
	print(x, "stands for", chr(x))

## list of list ##
 colors = ['red', 'blue', 'yellow', 'green']
 clothes = ['shirt', 'dress', 'skirt', 'shorts']

 closet = [colors, clothes]

 ## continet counter - RECURSION - no land on border ##
 
defdef​ continent_counter(world, x, y):
    ​ continent_count if​ world[y][x] != ​'land'​
 ​   # Either it's water or we already counted it,​
 ​   # but either way, we don't want to count it now.​
 ​   return​ 0
  
    # So first we count this tile...​
    size = 1
    world[y][x] = ​'counted land'​
    # ...then we count all of the neighboring eight tiles​
    # (and, of course, their neighbors by way of the recursion).​
    size = size + continent_counter(world, x-1, y-1)
    size = size + continent_counter(world, x , y-1)
    size = size + continent_counter(world, x+1, y-1)
    size = size + continent_counter(world, x-1, y )
    size = size + continent_counter(world, x+1, y )
    size = size + continent_counter(world, x-1, y+1)
    size = size + continent_counter(world, x , y+1)
    size = size + continent_counter(world, x+1, y+1)
    return size
​
print(continent_counter(world, 5, 5))