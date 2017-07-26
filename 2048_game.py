"""
2048 solver - 2048_game.py
----
This is the game itself that the solver will use to play.

Author: Ginotuch
"""

import os
from time import sleep
import random


def main():
    ## Commented out for testing
    # game_map = {}  # {3: [0, 0, 0, 0], 2: [0, 0, 0, 0], 1: [0, 0, 0, 0], 0: [0, 0, 0, 0]}
    # initialise_map_blank(game_map, 4)
    # choice = move_choice()
    # print(choice)

    # Testing game map
    game_map = {
        3: [2, 0, 0, 0],
        2: [0, 0, 0, 0],
        1: [0, 89746, 0, 0],
        0: [64, 4, 8, 0]}
    print_current(game_map)
    input()

    while True:  # Tests number generation
        add_number = new_num(game_map)
        if add_number is False:
            print("Game Over")
            break
        print_current(game_map)
        sleep(1)
    input()


def new_num(game_map):
    empty_slots = []
    for row in range(len(game_map.values())):
        for slot in range(len(game_map[row])):
            if game_map[row][slot] == 0:
                empty_slots += [(slot, row)]
    if len(empty_slots) < 1:
        return False
    if random.randrange(11) == 10:
        random_num = 4
    else:
        random_num = 2
    ran_num = (random_num, random.choice(empty_slots))  # creates a tuple with the random number, and random location
    game_map[ran_num[1][1]][ran_num[1][0]] = ran_num[0]  # Adds the random number to the board

    pass


def move_choice():
    choice = None
    while not choice:
        temp_choice = input("1-up, 2-down, 3-left, 4-right: ")
        try:
            if int(temp_choice) not in range(1, 5):
                print("fail")
        except ValueError:
            print("enter a number 1-4")
        else:
            choice = temp_choice
    return int(choice)


def initialise_map_blank(game_map, map_len):
    count = map_len - 1
    for x in range(map_len):
        game_map[count] = [0] * map_len
        count -= 1


def print_current(game_map):
    # print(".\n" * 20)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears console in windows/linux
    print()

    # Finds longest number
    biggest = 0
    for row in game_map.values():
        for item in row:
            if len(str(item)) > biggest:
                biggest = len(str(item))

    # Prints the board with Y index numbers.
    count = len(game_map.keys()) - 1
    spaces = len(str(count))
    for a in game_map.values():
        print(count, "  ", " " * (spaces - len(str(count))), end="")
        count -= 1
        for x in a:
            print(x, " " * ((biggest - len(str(x))) + 1), end="")
        print()
    print()

    # Printing X index numbers
    print("     ", end="")
    for x in range(len(game_map.keys())):
        print(x, " " * ((biggest - len(str(x))) - 1), end="  ")
    print()
    sleep(0.1)


def initialise_map_ran(game_map, map_len):
    count = map_len - 1
    for x in range(map_len):
        game_map[count] = [0] * map_len
        count -= 1


main()
