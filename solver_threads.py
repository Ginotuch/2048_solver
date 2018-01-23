"""
2048 solver - solver_threads.py
----
This is essentially the same as solver.py except it utilises
threading. Sadly this is mostly a test as the speed is essentially the same.

Author: Ginotuch
"""

from random import choice
from time import time
import threading
from game import GameMap


def main():
    past_scores = []
    start = time()
    stats = [0, 0]
    threads = []
    total_games = 20

    for x in range(total_games):
        t = threading.Thread(target=basic_solver, args=(past_scores, stats, 100))
        threads.append(t)

    for x in range(total_games):
        threads[x].start()

    for x in range(total_games):
        threads[x].join()

    end = time()
    print_stats(stats, past_scores, start, end)


def print_stats(stats, past_scores, start, end):
    total_time = (end - start)
    hours = int((total_time // 3600) // 60)
    total_time = total_time % 3600
    minutes = int(total_time // 60)
    seconds = round(total_time % 60, 3)
    milliseconds = str(round(seconds - int(seconds), 3))[2:]
    seconds = int(seconds)
    time_string = str(hours) + ":" + str(minutes) + ":" + str(seconds) + ":" + str(milliseconds)
    print("Time taken:", time_string)
    print("Total moves:", stats[0])
    print("Average score:", sum(past_scores) / len(past_scores))
    print("Out of", stats[1], "games, the highest score was:", max(past_scores))
    print("Lowest score:", min(past_scores))


def basic_solver(past_scores, stats, retries):
    game_map = GameMap()
    moved = False
    moves = 0
    games = 0
    while True:
        if not moved:
            temp = choice([(1, 2), (3, 4)])
            game_map.move(temp[0])
            moves += 1
            direction = temp[1]
        else:
            direction = choice([2, 3])
        moved = game_map.move(direction)
        stats[0] += 1
        if moved:
            game_map.new_num()
            continue
        elif not game_map.movement_check():
            past_scores += [game_map.score()]
            game_map = GameMap()
            games += 1
            stats[1] += 1
            if games == retries:
                break


main()
