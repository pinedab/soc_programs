import random
from sys import exit

def play(grid, rounds):
    ##make the solver
    print("Solver to be made")
    exit(0)

def rounds():
    num = input("How many rounds do you want to play?\n> ")
    return num


def old():
    old_board = {
        1: 'AACIOT', 2: 'AHMORS', 3: 'EGKLUY', 4: 'ABILITY',
        5: 'ACDEMP', 6: 'EGINTV', 7: 'GILRUW', 8: 'ELPSTU',
        9: 'DENOSW', 10: 'ACELRS', 11: 'ABJMOQ', 12: 'EEFHIY',
        13: 'EHINPS', 14: 'DKNOTU', 15: 'ADENVZ', 16: 'BIFORX'
    }
    return make_board(old_board)


def new():
    new_board = {
        1: 'AAEEGN', 2: 'ELRTTY', 3: 'AOOTTW', 4: 'ABBJOO',
        5: 'EHRTVW', 6: 'CIMOTU', 7: 'DISTTY', 8: 'EIOSST',
        9: 'DELRVY', 10: 'ACHOPS', 11: 'HIMNQU', 12: 'EEINSU',
        13: 'EEGHNW', 14: 'AFFKPS', 15: 'HLNNRZ', 16: 'DEILRX'
    }
    return make_board(new_board)


def make_board(die):
    grid = {}
    for x in range(4):
        for y in range(4):
            for d, sides in list(die.items()):
                grid[x, y] = sides[random.randrange(6)]
    game = []
    for key, val in list(grid.items()):
        game.append(val)

    # print(game)
    return game


def start():
    print("Hi, this is a Boggle Solver?")
    count = 0
    while True:
        # Choose a board type
        print("Do you want to play the new or the old version of Boggle?")
        choice = input("> ")
        if 'n' in choice:
            print("You have chosen the NEW version.")
            g = new()
            r = rounds()
            print(f"You want to play {r} rounds with the {choice} version. Great!\n\nHere is the grid:\n{g}")
            play(g, r)
            exit(0)
        elif 'o' in choice:
            print("You have chosen the OLD version.")
            g = old()
            r = rounds()
            print(f"You want to play {r} rounds with the {choice} version. Great!\n\nHere is the grid:\n{g}")
            play(g, r)
            exit(0)
        else:
            print("INVALID. Please pick a version.")
            if count > 1: #3 times idk why wtf
                print("Clearly, you don't want to play. Bye!")
                exit(0)
            count += 1

start()
