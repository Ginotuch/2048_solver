"""
2048 solver - solver.py
----
This is the solver, there will be two versions, the basic solver which
pretty much presses random buttons till it can't move anymore (although
with a little extra stuff).

Then there will be the Tree explorer, which will try to brute force the
game and find the highest score it can.

Author: Ginotuch
"""

from random import choice, randrange
from time import time
from game import GameMap


def main():
    game_map = GameMap()
    basic_solver(game_map, 2000)


def basic_solver(game_map, retries):
    past_scores = []
    highest_score = 0
    games = 0
    count = 0
    moved = False
    start = time()
    moves = 0
    while True:
        if not moved:
            direction = choice([1, 2, 3, 4])
        else:
            direction = choice([2, 3])
        moved = game_map.move(direction)
        moves += 1
        #game_map.print_current(False)  # Commented out as it slows down the code a huge amount
        if not game_map.movement_check():
            count += 1
            if count % 20 == 0:
                print("Games complete:", count)
            if game_map.game_map[1] > highest_score:
                highest_score = game_map.game_map[1]
            past_scores += [game_map.game_map[1]]
            game_map = GameMap()
            games += 1
            if games == retries:
                break
        if moved:
            game_map.new_num()
    end = time()
    total_time = (end - start)
    hours = int((total_time // 3600) // 60)
    total_time = total_time % 3600
    minutes = int(total_time // 60)
    seconds = round(total_time % 60, 3)
    milliseconds = str(round(seconds - int(seconds), 3))[2:]
    seconds = int(seconds)
    time_string = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(milliseconds)
    print("Time taken:", time_string)
    print("Total moves:", moves)
    print("Average score:", sum(past_scores) / len(past_scores))
    print("Out of", games, "games, the highest score was:", highest_score)
    print("Lowest score:", min(past_scores))


main()
