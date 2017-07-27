import game
from random import randrange
from copy import deepcopy
from time import sleep


def main():
    game_map = game.initialise_map_blank(4)
    database = [
        {"mv": 1,
         "dead": False,
         "map": [{}, 0],
         "next": []},

        {"mv": 2,
         "dead": False,
         "map": [{}, 0],
         "next": []}
    ]
    history = [0]
    highest_score = 0
    tries = 200
    while True:
        if game_map == history[-1]:
            direction = randrange(1, 5, 3)
        else:
            direction = randrange(2, 4)
        game.move(direction, game_map)
        history += [deepcopy(game_map)]
        game.print_current(game_map)
        if not game.movement_check(game_map):
            if game_map[1] > highest_score:
                highest_score = game_map[1]
            print("done")
            print("Saving stats and reinitialising board...")
            game_map = game.initialise_map_blank(4)
            print("restarting...")
            sleep(0.5)
            tries -= 1
            if tries == 0:
                break
        game.new_num(game_map)
    print("Out of 20 tries, the highest score was:", highest_score)

main()
