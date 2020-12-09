import sys

from app import NimGameApp

if __name__ == '__main__':
    piles = list(map(int, sys.argv[1:]))

    app = NimGameApp(piles)

    print(app.get_game_tree_as_json())
    print(app.get_solution_as_json())
