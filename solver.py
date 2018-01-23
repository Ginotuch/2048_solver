"""
2048 solver - solver.py
----
This is the solver, there will be two versions, the basic solver which
pretty much presses random buttons till it can't move anymore (although
with a little extra stuff).

Then there will be the Tree explorer, which will try to 'brute force' the
game and find the highest score it can.

Author: Ginotuch
"""

from random import choice
from time import time

from game import GameMap


def main():
    game_map = GameMap()
    basic_solver(game_map, 1000)


def basic_solver(game_map, retries):
    past_scores = []
    games = 0
    count = 0
    moved = False
    start = time()
    moves = 0
    total_moves = []
    while True:
        if not moved:
            temp = choice([(1, 2), (3, 4)])
            game_map.move(temp[0])
            moves += 1
            direction = temp[1]
        else:
            direction = choice([2, 3])
        moved = game_map.move(direction)
        moves += 1
        #game_map.print_current(True)  # Commented out as it slows down the code a huge amount
        if moved:
            game_map.new_num()
            continue
        elif not game_map.movement_check():
            count += 1
            if count % 20 == 0:
                print("Games complete:", count)
            past_scores += [game_map.score()]
            game_map = GameMap()
            total_moves += [moves]
            moves = 0
            games += 1
            if games == retries:
                break
    end = time()
    total_time = (end - start)
    hours = int((total_time // 3600) // 60)
    total_time = total_time % 3600
    minutes = int(total_time // 60)
    seconds = round(total_time % 60, 3)
    milliseconds = str(round(seconds - int(seconds), 3))[2:]
    seconds = int(seconds)
    time_string = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(milliseconds)
    print("\n\n\nTime taken:", time_string)
    print("Average moves:", sum(total_moves) // len(total_moves))
    print("Most moves:", max(total_moves))
    print("Least moves:", min(total_moves))
    print("Average score:", sum(past_scores) // len(past_scores))
    print("Out of", games, "games, the highest score was:", max(past_scores))
    print("Lowest score:", min(past_scores))


main()
