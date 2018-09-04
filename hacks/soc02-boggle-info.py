# Challenge: Write a boggle solver that finds all possible
# words on a given board.  You should pick a fixed vocabulary
# (dictionary) - dict.txt


# GIVEN A BOGGLE BOARD?
# NO, MAKE THE BOGGLE BOARD
#   4x4 = 16 die?
#   DO I WANT A RANDOM BOGGLE BOARD OPTION?
#            import random
#            from string import ascii_uppercase
#            grid={}
#            for x in range(4):
#                    for y in range(4):
#                        grid[x,y]=random.choice(ascii_uppercase)
#            print(grid)
# SHAKE OPTION
# START 3MIN CLOCK
# COLLECT ALL INPUTS IN LIST? NO
# 
# POINT SYSTEM:
#    1/2 letter words = 0 points 
#    3 letter words = 1 point 
#    4 letter words = 2 points 
#    5 letter words = 3 points
#    The longest possible word 16 letter word = 14 points
#   
# TIME IS UP - CALCULATE POINTS? NO
# CALCULATE MOST POSSIBLE POINTS
# CODE SHOULD RETURN
# result = {
#     "score": 143,
    # "words": [ "" , "", "", "", ... , ""] #abc order
# }

# 
# # BONUSES:
# fastest algorithm
# choose dictionary
# choose dice distribution
# extend to 3x3 and 5x5