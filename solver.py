from copy import deepcopy
from random import randrange

import game


def main():
    game_map = game.initialise_map_blank(4)
    database = [  # Example of what the database might look like
        [{}, 0],  # game map
        {
            "mv": 1,
            "gover": False,
            "map": [{}, 0],
            "next": []},

        {
            "mv": 2,
            "gover": False,
            "completed":False,
            "map": [{}, 0],
            "next": []}
    ]
    previous_move = None
    past_scores = []
    highest_score = 0
    games = 0
    count = 0
    while True:
        if game_map == previous_move:
            direction = randrange(1, 5, 3)
        else:
            direction = randrange(2, 4)
        game.move(direction, game_map)
        previous_move = deepcopy(game_map)
        #game.print_current(game_map) # Commented out as it slows down the code a huge amount
        if not game.movement_check(game_map):
            count += 1
            if count % 20 == 0:
                print("Games complete:", count)
            if game_map[1] > highest_score:
                highest_score = game_map[1]
            previous_move = deepcopy(game_map)
            past_scores += [game_map[1]]
            game_map = game.initialise_map_blank(4)
            games += 1
            if games == 2000:
                break
        game.new_num(game_map)
    print("Average score:", sum(past_scores) / len(past_scores))
    print("Out of", games, "games, the highest score was:", highest_score)
    input()


main()
