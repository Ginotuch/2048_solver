from copy import deepcopy
from random import randrange

import game


def main():
    game_map = game.initialise_map_blank(4)
    database = [
        {
            "mv": 1,
            "dead": False,
            "map": [{}, 0],
            "next": []},

        {
            "mv": 2,
            "dead": False,
            "map": [{}, 0],
            "next": []}
    ]
    history = [0]
    highest_score = 0
    games = 0
    count = 0
    while True:
        if game_map == history[-1]:
            direction = randrange(1, 5, 3)
        else:
            direction = randrange(2, 4)
        game.move(direction, game_map)
        history += [deepcopy(game_map)]
        # game.print_current(game_map) # Commented out as it slows down the code a huge amount
        if not game.movement_check(game_map):
            count += 1
            if count % 20 == 0:
                print("Games complete:", count)
            if game_map[1] > highest_score:
                highest_score = game_map[1]
            game_map = game.initialise_map_blank(4)
            games += 1
            if games == 2000:
                break
        game.new_num(game_map)
    print("Out of", games, "games, the highest score was:", highest_score)


main()
