from StateNode import StateNode
from core import solve, search_for_winning_move


class NimGameApp:
    def __init__(self, piles: [int]):
        self.root_state = StateNode()
        self.solution_dict = dict()
        self.pile_counts = piles

        self.__solve()

    def __solve(self):
        solve(
            piles=self.pile_counts,
            current_state_node=self.root_state,
            solution_dict=self.solution_dict
        )

    def search_for_winning_move(self):
        return ",".join(map(str, search_for_winning_move(
            state=self.pile_counts,
            solution_dict=self.solution_dict
        )))

    def move(self, row_index: int, number_of_takes: int):
        self.pile_counts[row_index] -= number_of_takes

    def __solution_as_json(self):
        ret = {}
        for state, solution in self.solution_dict.items():
            state_string = ",".join(map(str, state))
            solution_string = ",".join(map(str, solution))

            ret[state_string] = solution_string

        return ret

    def __game_tree_as_json(self):
        return self.root_state.to_json()

    def get_game_tree_as_json(self):
        return self.__game_tree_as_json()

    def get_solution_as_json(self):
        return self.__solution_as_json()
