# Exercise 36 - Make my own adventure
from sys import exit
STICK = False
DOG = False
RETURNED = False


def next():
    print("Where do you want to investigate next? Front of the train, back of the train, or the seats again?")
    choice = input("> ")

    if 'front' in choice:
        monster()
    elif 'back' in choice:
        source()
    else:
        dead("How the heck does that make sense. Because you were messing around you died since the monster took the opportunity to send its' mutant spider babies to get ya.")


def barricade():
    print("Running for your life, you get through the door.")
    print("Do you want to continue running or block the door?")
    while True:
        choice = input("> ")
        if 'running' in choice:
            dead("You skipped gym class. The monster overtakes you, and you die by being clawed to death.")
        elif not STICK and 'block' in choice:
            dead("You have nothing to block the door with, bro. The monster busts the door open and rips your limbs apart for being dumb.")
        elif 'block' and STICK:
            print("You block the door with the hockey stick and eventually figure out how to",
                  "unhook your carriage from the rest of train.")
            if DOG:
                print("You and the dog survive and wait for help to come.")
                exit(0)
            else:
                print("Because you didn't save the dog, you die from starvation.")
                exit(0)
        else:
            print("That doesn't make sense.")


def monster():
    print("You decide to summon all your courage and go in the direction of the monster.")
    print("Walking through the door, you see the grotesque monster chewing on a leg as",
          "its scales ooze acid onto the seats.")
    print("As fear tingles your spine, you can either 'fight', 'run', or 'hide'?")
    choice = input("What is your choice?\n> ")
    if 'hide' in choice:
        dead('You decided to hide when the monster already heard you. Clearly, you got eaten.')
    elif STICK and DOG:
        if 'fight' in choice:
            print("You decide to fight with the hockey stick and your new best friend.")
            print("After slicing through the monster before it regenerates you get to,"
                  "the control room")
            control_room()
        elif 'run' in choice:
            barricade()
        else:
            dead("That didn't work so you get swallowed head first for trying bad ideas.")

    elif DOG and not STICK:
        if 'fight' in choice:
            print("You decide to fight with the cutest puppy.")
            print("You can 'throw the dog' or 'scream with the dog'?")
            c = input("> ")
            if 'throw' in c:
                dead("You are a terrible human being. You deserve to suffer as the monster slowly strips the flesh from your bones.")
            elif 'scream' in c:
                dead("You've irritated the monster so it sits on you to suffocate the noise. Because of your folly, the dog dies too.")
            elif 'run' in choice:
                barricade()
            else:
                dead(
                    "That didn't work so you get swallowed head first for trying bad ideas.")

    elif not STICK and not DOG:
        if 'fight' in choice:
            dead(
                "You rush into battle barefisted and brave. Obviously you die. What were you thinking?")
        elif 'run' in choice:
            barricade()

    else:
        dead("You suck, the monster spots and charges at you. It finds your organs delicious.")


def source():
    print("You have decided to investigate the back of the train.")
    print("There is blood and guts staining the windows and the seats. You reach the last cart.")
    print("No one is left except for something shuffling behind a pile of blankets and jackets.")
    print("Do you kick it, reveal it, or go back to your seat?")
    choice = input("> ")

    if 'kick' in choice:
        dead("'YOWLOOOH' goes the dog under the pile. The monster hears it and returns to eat you, the prick, that kicked an innocent doggo.")
    elif 'reveal' in choice:
        print("You remove the pile and find a dog and a hockey stick.")
        stuff = input("Do you want the 'dog', the hockey 'stick', or 'none'?\n> ")
        if 'dog' in stuff:
            dead("GRRRRRR.. you back off as it continues to bark its head off. As you cower away, the monster sneaks up behind you and devours your soul.")
        elif 'stick' in stuff:
            DOG = True
            STICK = True
            back_seat("You take the stick, and as you try to leave the dog begins to follow. You've made a new friend.")
        elif 'none' in stuff:
            print("You head back to your seat, but the dog follows you quietly because it is scared and now ownerless.")
            print("However, when you get toyour seat you realize it has all been a dream, except for the dog.")
            print("As you fully awaken to the licks of the dog, you realize the events of the dream are taking place.")
            back_seat("As the people run past, the dog runs away, as well, since you are awake now.")
        else:
            print(stuff)
    elif 'seat' in choice:
        dead("You left the pile alone, and trip on your way back to your seat. The monster hears and comes back to skin you alive.")
    else:
        print("That didn''t work.")
        source()


def investigate():
    print()
    if RETURNED and DRINK:
        print("The only thing left to do is go to the front of the train.")
        c = input("> ")
        monster()

    else:
        print("You have decided to investigate what the actual crackers is going on.",
              " You can travel towards the back of the train or check the seats.")
        choice = input("> ")

        while True:
            if 'back' in choice:
                source()
            elif 'check' in choice or 'seats' in choice:
                print("Congrats, there is a monster on the loose",
                      "and you found some whiskey for this dire situation. Care for a drink? y/n")
                choice = input("> ")
                if 'y' in choice:
                    DRINK = False
                    print(
                        "That was a little too good, so you drank it up and are now inebriated.")
                elif 'n' in choice:
                    DRINK = True
                    print("Save it for later then.")
                    next()
                else:
                    print("Sorry, not an option.")
            else:
                dead("That didn't work.")


def stay():
    if RETURNED:
        print("You have decided to hide under a blanket and stay put.")
        print("From under a blanket, you sense something smelly and large slither past you.")

    print("With a sigh of relief, you can either 'stay' put, go 'investigate' the monster, or get up and 'look' around?")
    choice = input("> ")

    if "stay" in choice and not RETURNED:
        start()
    elif "investigate" in choice:
        if STICK == False:
            dead("The monster is waiting for you and melts you into a puddle.")
        else:
            monster()
    elif "look" in choice:
        investigate()
    else:
        dead("That didn't work.")
        stay()


def dead(why):
    print(why, "Great job!")
    exit(0)


def back_seat(why):
    print(why, "You are now back at your seat.")
    RETURNED = True
    stay()


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
