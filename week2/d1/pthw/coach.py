from sys import exit

STICK = False
DOG = False
DRANK = False
RETURNED = False

# def investigate():


def barricade():
    print()
    print("Running for your life, you get through the door of the previous cart.")
    print("Do you want to continue 'running' or 'block' the door?")
    count = 0
    while True:
        choice = input("> ")
        if 'running' in choice:
            dead("You skipped gym class. The monster overtakes you, and you die by being clawed to death.")
        elif not STICK and 'block' in choice:
            dead("You have nothing to block the door with, bro. The monster busts the door open and rips your limbs apart for being dumb.")
        elif 'block' and STICK in choice:
            print("You block the door with the hockey stick and eventually figure out how to",
                  "unhook your carriage from the rest of train.")
            if DOG:
                print("You and the dog survive and wait for help to come.")
                exit(0)
            else:
                print("Because you didn't rescue the dog this time, you die from starvation.")
                exit(0)
        else:
            if count < 3:
                print("That doesn't make sense.")
                count += 1
            else:
                print("Your options weren't that difficult, but you still took so long.")
                dead(" The monster caught up to you, and decided to use you as floss.")


def monster():
    print()
    print("You decide to summon all your courage and go in the direction of the monster.")
    print("Walking through the door, you see the grotesque monster chewing on a leg as its scales ooze acid onto the carcasses of other passengers.")
    print("As fear tingles your spine, you can either 'fight' the monster, 'run' away, or 'hide'?")

    choice = input("What is your choice?\n> ")
    if 'fight' in choice:
        if not STICK and not DOG:
            dead(
                "You rush into battle barefisted and brave. Obviously you die. What were you thinking?")
    elif 'run' in choice:
        barricade()
    elif 'hide' in choice:
        if not STICK and not DOG:
            dead(
                'You decided to hide when the monster already heard you. Clearly, you got eaten.')


def stay():
    print()
    count = 0
    while True:
        print("You hold your breathe, hoping the monster doesn't come back, but you can't hold out forever...")
        print("What wil you do next? Do you want to 'stay' as you are, 'follow' the monster, or 'look' around you?")
        choice = input("> ")
        if 'stay' in choice:
            count += 1
        elif 'follow' in choice:
            monster()
        elif 'look' in choice:
            investigate()
        else:
            print("You gotta do something, bro.")
            count += 1

        if count > 3:
            print()
            dead("Your hesitation cost you your life. Make better decisions in the future")


def dead(why):
    print(why, "Great job!")
    exit(0)


def start():
    print("You have just arrived on the train for your",
          "daily commute to Chestery.")
    print("You take a seat and begin to doze off.")
    print("You awaken to people rushing past your seat.")
    print("Do you 'hide' in your seat,",
          "'run' with the crowd, or 'investigate' what's going on?")

    choice = input("> ")

    if 'hide' in choice:
        stay()
    elif 'run' in choice:
        dead("You decide to make a run for it. Too bad, you get trampled by a stampede of terrified people.")
    elif 'investigate' in choice:
        investigate()
    else:
        dead("That didn't work. You starved to death on the train. Forgotten by everyone!")


start()
