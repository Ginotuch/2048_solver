import game
from random import randrange


def main():
    initial_map = game.initialise_map_blank(4)
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
    while True:
        choices = [2,2,2,2,2,2,2,3,3,3,3,3,3,3,2,2,3,3,1,4,1,1,4,4]
        game.move(choices[randrange(len(choices))], initial_map)
        game.print_current(initial_map)
        if not game.movement_check(initial_map):
            print("done")
            input()
            break
        game.new_num(initial_map)


main()
