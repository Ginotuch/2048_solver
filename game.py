"""
2048 solver - game.py
----
This is the game itself that the solver will use to play.

Author: Ginotuch
"""

from os import system, name
from random import randrange, choice
from time import sleep


class GameMap:
    def __init__(self):
        game_map = [[], 0]
        for x in range(4):
            game_map[0] += [[0] * 4]
        self.game_map = game_map
        self.new_num()
        self.new_num()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def new_num(self):
        empty_slots = []
        for row in range(len(self.game_map[0])):
            for slot in range(len(self.game_map[0][row])):
                if self.game_map[0][row][slot] == 0:
                    empty_slots += [(slot, row)]
        if len(empty_slots) < 1:
            return False
        if randrange(10) == 9:
            random_num = 4
        else:
            random_num = 2
        ran_num = (random_num, choice(empty_slots))  # creates a tuple with the random number, and random location
        self.game_map[0][ran_num[1][1]][ran_num[1][0]] = ran_num[0]  # Adds the random number to the board

    def score(self):
        return self.game_map[1]

    def print_current(self, sleep_o):
        system('cls' if name == 'nt' else 'clear')  # Clears console in windows/linux (This breaks when using PyCharm)
        print()
        print("Score: ", self.score())
        print()
        # Finds longest number
        biggest = 1
        for row in self.game_map[0]:
            for item in row:
                if len(str(item)) > biggest:
                    biggest = len(str(item))

        # Prints the board with Y index numbers.
        count = len(self.game_map[0]) - 1
        spaces = len(str(count))
        for a in self.game_map[0]:
            print(count, "  ", " " * (spaces - len(str(count))), end="")
            count -= 1
            for x in a:
                print(x, " " * ((biggest - len(str(x))) + 1), end="")
            print()
        if sleep_o:
            sleep(0.1)  # Makes it readable when AI is making moves
        print()

        # Printing X index numbers
        print("     ", end="")
        for x in range(len(self.game_map[0])):
            spaces = " " * (biggest - len(str(x)) + 1)
            print(x, spaces, end="")
        print()

    def movement_check(self):
        for row in self.game_map[0]:  # quick blank slot check
            for item in row:
                if item == 0:
                    return True

        cur_check = True
        # Checks left/right only if the above doesn't return True (Saves a shit ton of time)
        for row in range(len(self.game_map[0])):
            for item in range(len(self.game_map[0][row])):
                if 0 < item < 3:
                    if self.game_map[0][row][item] == self.game_map[0][row][item + 1] or self.game_map[0][row][item] == \
                            self.game_map[0][row][item - 1]:
                        return True
                elif item == 3:
                    if self.game_map[0][row][item] == self.game_map[0][row][item - 1]:
                        return True
                elif item == 0:
                    if self.game_map[0][row][item] == self.game_map[0][row][item + 1]:
                        return True
                cur_check = False

        # Checks up/down
        for item in range(len(self.game_map[0][0])):
            for row in range(len(self.game_map[0]) - 1, -1, -1):
                if 0 < row < 3:
                    if self.game_map[0][row][item] == self.game_map[0][row + 1][item] or self.game_map[0][row][item] == \
                            self.game_map[0][row - 1][item]:
                        return True
                elif row == 3:
                    if self.game_map[0][row][item] == self.game_map[0][row - 1][item]:
                        return True
                elif row == 0:
                    if self.game_map[0][row][item] == self.game_map[0][row + 1][item]:
                        return True
                cur_check = False
        return cur_check

    def move(self, direction):
        moved = False
        # directions = {
        #     1: "up",
        #     2: "down",
        #     3: "left",
        #     4: "right"
        # }
        if direction == 2:  # down (This used to be up, it's now down, I don't know why)
            for item in range(len(self.game_map[0][0])):
                for row in range(len(self.game_map[0]) - 1, -1, -1):
                    if self.game_map[0][row][item] != 0:
                        end = False
                        while not end:
                            if row == 3:
                                end = True
                                break
                            elif self.game_map[0][row + 1][
                                item] == 0:  # Moved to new spot if the spot contains no numbers
                                self.game_map[0][row + 1][item] = self.game_map[0][row][item]
                                self.game_map[0][row][item] = 0
                                row += 1
                                moved = True
                                if row >= 3:
                                    end = True
                                    break

                            elif self.game_map[0][row + 1][item] == self.game_map[0][row][
                                item]:  # Adds two numbers and merges
                                self.game_map[0][row + 1][item] = self.game_map[0][row + 1][item] * 2
                                self.game_map[0][row][item] = 0
                                self.game_map[1] += self.game_map[0][row + 1][item]
                                moved = True
                                end = True
                            else:
                                end = True
                            if row == -1 or row == 4 or item == -1 or item == 4:
                                end = True

        elif direction == 1:  # up
            for item in range(len(self.game_map[0][0])):
                for row in range(1, len(self.game_map[0])):
                    if self.game_map[0][row][item] != 0:
                        end = False
                        while not end:
                            if row == 0:
                                end = True
                                break
                            elif self.game_map[0][row - 1][item] == 0:
                                self.game_map[0][row - 1][item] = self.game_map[0][row][item]
                                self.game_map[0][row][item] = 0
                                row -= 1
                                moved = True
                                if row <= 0:
                                    end = True
                                    break

                            elif self.game_map[0][row - 1][item] == self.game_map[0][row][item]:
                                self.game_map[0][row - 1][item] = self.game_map[0][row - 1][item] * 2
                                self.game_map[0][row][item] = 0
                                self.game_map[1] += self.game_map[0][row - 1][item]
                                moved = True
                                end = True
                            else:
                                end = True
                            if row == -1 or row == 4 or item == -1 or item == 4:
                                end = True

        elif direction == 3:  # left
            for row in self.game_map[0]:
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
                                self.game_map[1] += row[item - 1]
                                moved = True
                                end = True
                            else:
                                end = True
                            if row == -1 or row == 4 or item == -1 or item == 4:
                                end = True

        elif direction == 4:  # right
            for row in self.game_map[0]:
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
                                self.game_map[1] += row[item + 1]
                                moved = True
                                end = True
                            else:
                                end = True
                            if row == -1 or row == 4 or item == -1 or item == 4:
                                end = True
        return moved


def main():
    game_map = GameMap()

    while True:
        game_map.print_current(False)
        if not game_map.movement_check():
            print("GAME OVER")
            input()
            break
        moved = game_map.move(move_choice())
        if moved:
            game_map.new_num()


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


if __name__ == "__main__":
    main()
