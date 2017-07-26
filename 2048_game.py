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
    game_map = [{}, 0]  # [{3: [0, 0, 0, 0], 2: [0, 0, 0, 0], 1: [0, 0, 0, 0], 0: [0, 0, 0, 0]}, 0(score)]
    initialise_map_blank(game_map, 4)
    # choice = move_choice()
    # print(choice)

    # Testing game map
    # game_map = [{
    #     3: [2, 0, 0, 2],
    #     2: [2, 2, 2, 2],
    #     1: [0, 89746, 0, 0],
    #     0: [64, 4, 8, 8]}, 0]
    while True:
        print_current(game_map)
        move(move_choice(), game_map)

    # while True:  # Tests number generation
    #     add_number = new_num(game_map)
    #     if add_number is False:
    #         print("Game Over")
    #         break
    #     print_current(game_map)
    #     sleep(1)


def move(direction, game_map):
    score = 0
    directions = {
        1: "up",
        2: "down",
        3: "left",
        4: "right"
    }
    if direction == 1:  # up
        pass

    elif direction == 2:  # down
        pass

    elif direction == 3:  # left
        for row in game_map[0].values():
            for item in range(1, len(row)):
                if row[item] != 0:
                    end = False
                    while not end:
                        if item == 0:
                            end = True
                            break
                        elif row[item - 1] == 0:
                            row[item - 1] = row[item]
                            row[item] = 0
                            item -= 1

                        elif row[item - 1] == row[item]:
                            row[item - 1] = row[item - 1] * 2
                            row[item] = 0
                            score += row[item - 1] * 2
                            end = True
                        else:
                            end = True

        empty_count = 0
        for row in game_map[0].values():
            for item in row:
                if item == 0:
                    empty_count += 1

    elif direction == 4:  # right
        for row in game_map[0].values():
            for item in range(len(row) - 1, -1, -1):
                print(item)
                if row[item] != 0:
                    end = False
                    while not end:
                        if item == 3:
                            end = True
                            break
                        elif row[item + 1] == 0:
                            row[item + 1] = row[item]
                            row[item] = 0
                            item += 1

                        elif row[item + 1] == row[item]:
                            row[item + 1] = row[item + 1] * 2
                            row[item] = 0
                            score += row[item + 1] * 2
                            end = True
                        else:
                            end = True
    new_num(game_map)
    return score


def new_num(game_map):
    empty_slots = []
    for row in range(len(game_map[0].values())):
        for slot in range(len(game_map[0][row])):
            if game_map[0][row][slot] == 0:
                empty_slots += [(slot, row)]
    if len(empty_slots) < 1:
        return False
    if random.randrange(11) == 10:
        random_num = 4
    else:
        random_num = 2
    ran_num = (random_num, random.choice(empty_slots))  # creates a tuple with the random number, and random location
    game_map[0][ran_num[1][1]][ran_num[1][0]] = ran_num[0]  # Adds the random number to the board


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
        game_map[0][count] = [0] * map_len
        count -= 1
    new_num(game_map)


def print_current(game_map):
    # print(".\n" * 20)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears console in windows/linux (This breaks when using PyCharm)
    print()

    # Finds longest number
    biggest = 0
    for row in game_map[0].values():
        for item in row:
            if len(str(item)) > biggest:
                biggest = len(str(item))

    # Prints the board with Y index numbers.
    count = len(game_map[0].keys()) - 1
    spaces = len(str(count))
    for a in game_map[0].values():
        print(count, "  ", " " * (spaces - len(str(count))), end="")
        count -= 1
        for x in a:
            print(x, " " * ((biggest - len(str(x))) + 1), end="")
        print()
    print()

    # Printing X index numbers
    print("     ", end="")
    for x in range(len(game_map[0].keys())):
        print(x, " " * ((biggest - len(str(x))) - 1), end="  ")
    print()
    sleep(0.1)


def initialise_map_ran(game_map, map_len):
    count = map_len - 1
    for x in range(map_len):
        game_map[count] = [0] * map_len
        count -= 1


main()
