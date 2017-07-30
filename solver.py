from copy import deepcopy
from random import choice, randrange

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
    while True:
        if not moved:
            direction = choice([1, 2, 3, 4])
        else:
            direction = choice([2, 3])
        moved = game_map.move(direction)
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
    print("Average score:", sum(past_scores) / len(past_scores))
    print("Out of", games, "games, the highest score was:", highest_score)


main()
