from copy import deepcopy
from random import randrange, choice

from game import GameMap


def main():
    game_map = GameMap()
    database = [  # Example of what the database might look like
        [{}, 0],  # game map
        {
            "mv": 1,
            "gover": False,
            "completed": False,
            "map": [{}, 0],
            "next": []},

        {
            "mv": 2,
            "gover": False,
            "completed":False,
            "map": [{}, 0],
            "next": []},

        {
            "mv": 3,
            "gover": False,
            "completed": False,
            "map": [{}, 0],
            "next": []},

        {
            "mv": 4,
            "gover": False,
            "completed": False,
            "map": [{}, 0],
            "next": []}]
    basic_solver(game_map, 2000)


def basic_solver(game_map, retries):
    previous_move = None
    past_scores = []
    highest_score = 0
    games = 0
    count = 0

    while True:
        if game_map.game_map == previous_move:
            direction = choice([1,2,3,4])
        else:
            direction = choice([2, 3])
        moved = game_map.move(direction)
        previous_move = deepcopy(game_map.game_map)
        # game_map.print_current(False)  # Commented out as it slows down the code a huge amount
        if not game_map.movement_check():
            count += 1
            if count % 20 == 0:
                print("Games complete:", count)
            if game_map.game_map[1] > highest_score:
                highest_score = game_map.game_map[1]
            previous_move = deepcopy(game_map.game_map)
            past_scores += [game_map.game_map[1]]
            game_map = GameMap()
            games += 1
            if games == retries:
                break
        if moved:
            game_map.new_num()
    print("Average score:", sum(past_scores) / len(past_scores))
    print("Out of", games, "games, the highest score was:", highest_score)
    print("average")


main()
