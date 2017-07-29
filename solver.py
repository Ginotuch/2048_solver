from copy import deepcopy
from random import randrange

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

    # First does left/down movement a few times, then sets this True, to do a random up/down movement.
    step_1_random = False

    while True:
        if game_map == previous_move:  # Heavily under WIP
            if not step_1_random:
                for x in range(1, 3):
                    game_map.move(x)
                step_1_random = True
                continue
            elif step_1_random:
                direction = randrange(1, 5, 3)
                oposite_direction = 2 if direction == 1 else 3
                game_map.move(direction)
                game_map.move(oposite_direction)
                step_1_random = False
                continue
        else:
            direction = randrange(2, 4)
        game_map.move(direction)
        previous_move = deepcopy(game_map)
        #game.print_current(game_map) # Commented out as it slows down the code a huge amount
        if not game_map.movement_check():
            count += 1
            if count % 20 == 0:
                print("Games complete:", count)
            if game_map.game_map[1] > highest_score:
                highest_score = game_map.game_map[1]
            previous_move = deepcopy(game_map)
            past_scores += [game_map.game_map[1]]
            game_map = GameMap()
            games += 1
            if games == retries:
                break
        game_map.new_num()
    print("Average score:", sum(past_scores) / len(past_scores))
    print("Out of", games, "games, the highest score was:", highest_score)
    print("average")


main()
