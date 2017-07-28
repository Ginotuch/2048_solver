"""
2048 solver - game.py
----
This is the game itself that the solver will use to play.

Author: Ginotuch
"""

from os import system, name
from random import randrange, choice


def main():
    game_map = initialise_map_blank(4)

    while True:
        print_current(game_map)
        if not movement_check(game_map):
            print("GAME OVER")
            input()
            break
        moved = move(move_choice(), game_map)
        if moved:
            new_num(game_map)


def movement_check(game_map):
    for row in game_map[0].values():  # quick blank slot check
        for item in row:
            if item == 0:
                return True

    # Checks left/right
    for row in range(len(game_map[0].values())):
        for item in range(len(game_map[0][row])):
            if 0 < item < 3:
                if game_map[0][row][item] == game_map[0][row][item + 1] or game_map[0][row][item] == game_map[0][row][
                            item - 1]:
                    return True
            elif item == 3:
                if game_map[0][row][item] == game_map[0][row][item - 1]:
                    return True
            elif item == 0:
                if game_map[0][row][item] == game_map[0][row][item + 1]:
                    return True
            else:
                return False

    # Checks up/down
    for item in range(len(game_map[0][0])):
        for row in range(len(game_map[0]) - 1, -1, -1):
            if 0 < row < 3:
                if game_map[0][row][item] == game_map[0][row + 1][item] or game_map[0][row][item] == \
                        game_map[0][row - 1][item]:
                    return True
            elif row == 3:
                if game_map[0][row][item] == game_map[0][row - 1][item]:
                    return True
            elif row == 0:
                if game_map[0][row][item] == game_map[0][row + 1][item]:
                    return True
            else:
                return False


def move(direction, game_map):
    moved = False
    directions = {
        1: "up",
        2: "down",
        3: "left",
        4: "right"
    }
    if direction == 1:  # up
        for item in range(len(game_map[0][0])):
            for row in range(len(game_map[0]) - 1, -1, -1):
                if game_map[0][row][item] != 0:
                    end = False
                    while not end:
                        if row == 3:
                            end = True
                            break
                        elif game_map[0][row + 1][item] == 0:  # Moved to new spot if the spot contains no numbers
                            game_map[0][row + 1][item] = game_map[0][row][item]
                            game_map[0][row][item] = 0
                            row += 1
                            moved = True
                            if row >= 3:
                                end = True
                                break

                        elif game_map[0][row + 1][item] == game_map[0][row][item]:  # Adds two numbers and merges
                            game_map[0][row + 1][item] = game_map[0][row + 1][item] * 2
                            game_map[0][row][item] = 0
                            game_map[1] += game_map[0][row + 1][item]
                            moved = True
                            end = True
                        else:
                            end = True
                        if row == -1 or row == 4 or item == -1 or item == 4:
                            end = True

    elif direction == 2:  # down
        for item in range(len(game_map[0][0])):
            for row in range(1, len(game_map[0])):
                if game_map[0][row][item] != 0:
                    end = False
                    while not end:
                        if row == 0:
                            end = True
                            break
                        elif game_map[0][row - 1][item] == 0:
                            game_map[0][row - 1][item] = game_map[0][row][item]
                            game_map[0][row][item] = 0
                            row -= 1
                            moved = True
                            if row <= 0:
                                end = True
                                break

                        elif game_map[0][row - 1][item] == game_map[0][row][item]:
                            game_map[0][row - 1][item] = game_map[0][row - 1][item] * 2
                            game_map[0][row][item] = 0
                            game_map[1] += game_map[0][row - 1][item]
                            moved = True
                            end = True
                        else:
                            end = True
                        if row == -1 or row == 4 or item == -1 or item == 4:
                            end = True

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
                            moved = True
                            if item <= 0:
                                end = True
                                break

                        elif row[item - 1] == row[item]:
                            row[item - 1] = row[item - 1] * 2
                            row[item] = 0
                            game_map[1] += row[item - 1]
                            moved = True
                            end = True
                        else:
                            end = True
                        if row == -1 or row == 4 or item == -1 or item == 4:
                            end = True

    elif direction == 4:  # right
        for row in game_map[0].values():
            for item in range(len(row) - 1, -1, -1):
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
                            moved = True
                            if item >= 3:
                                end = True
                                break

                        elif row[item + 1] == row[item]:
                            row[item + 1] = row[item + 1] * 2
                            row[item] = 0
                            game_map[1] += row[item + 1]
                            moved = True
                            end = True
                        else:
                            end = True
                        if row == -1 or row == 4 or item == -1 or item == 4:
                            end = True
    return moved


def new_num(game_map):
    empty_slots = []
    for row in range(len(game_map[0].values())):
        for slot in range(len(game_map[0][row])):
            if game_map[0][row][slot] == 0:
                empty_slots += [(slot, row)]
    if len(empty_slots) < 1:
        return False
    if randrange(11) == 10:
        random_num = 4
    else:
        random_num = 2
    ran_num = (random_num, choice(empty_slots))  # creates a tuple with the random number, and random location
    game_map[0][ran_num[1][1]][ran_num[1][0]] = ran_num[0]  # Adds the random number to the board


def move_choice():
    choice = None
    while not choice:
        temp_choice = input("1/W-up, 2/S-down, 3/A-left, 4/D-right: ")
        try:
            if int(temp_choice) not in range(1, 5):
                print("fail")
        except ValueError:
            if temp_choice.lower() in 'wasd':
                if temp_choice.lower() == 'w':
                    choice = 1
                elif temp_choice.lower() == 'a':
                    choice = 3
                elif temp_choice.lower() == 's':
                    choice = 2
                elif temp_choice.lower() == 'd':
                    choice = 4
            print("enter a number 1-4")
        else:
            choice = int(temp_choice)
    return choice


def initialise_map_blank(map_len):
    game_map = [{}, 0]
    count = map_len - 1
    for x in range(map_len):
        game_map[0][count] = [0] * map_len
        count -= 1
    new_num(game_map)
    new_num(game_map)
    return game_map


def print_current(game_map):
    system('cls' if name == 'nt' else 'clear')  # Clears console in windows/linux (This breaks when using PyCharm)
    print()
    print("Score: ", game_map[1])
    print()
    # Finds longest number
    biggest = 1
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
        spaces = " " * (biggest - len(str(x)) + 1)
        print(x, spaces, end="")
    print()


def initialise_map_ran(game_map, map_len):
    count = map_len - 1
    for x in range(map_len):
        game_map[count] = [0] * map_len
        count -= 1

if __name__ == "__main__":
    main()
