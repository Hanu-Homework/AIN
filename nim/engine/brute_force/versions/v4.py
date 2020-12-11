from typing import List, Tuple, Dict, Union

class StateNode:
    def __init__(self):
        self.move: Tuple[int, int] = (0, 0)
        self.is_winning: Union[bool, None] = None
        self.children: List[StateNode] = []


def solve(
        piles: List[int],
        current_state_node: StateNode,
        solution_dict: Dict[Tuple[int, ...], Tuple[int, int]],
        is_my_turn: bool=True,
        visited_states: Dict[Tuple[Tuple[int, ...], bool], bool]=None
) -> bool:
    if visited_states is None:
        visited_states = dict()
    if sum(piles) == 0:
        return not is_my_turn

    state_notation = (tuple(sorted(piles)), is_my_turn)
    if state_notation in visited_states:
        return visited_states[state_notation]
    result = not is_my_turn

    is_result_determined = False

    for pile_index in range(len(piles)):
        if is_result_determined:
            break
        for number_of_takes in range(1, piles[pile_index] + 1):
            if is_result_determined:
                break
            new_piles = piles.copy()
            new_piles[pile_index] -= number_of_takes
            new_state_node = StateNode()
            new_state_node.move = (pile_index, number_of_takes)
            current_state_node.children.append(new_state_node)
            winning = solve(new_piles, new_state_node, solution_dict, not is_my_turn, visited_states)
            new_state_node.is_winning = winning
            if is_my_turn and winning:
                result = True
                is_result_determined = True
                pile_index_in_sorted_state = state_notation[0].index(piles[pile_index])
                solution_move = (pile_index_in_sorted_state, number_of_takes)
                solution_dict[state_notation[0]] = solution_move
            elif not is_my_turn and not winning:
                result = False
                is_result_determined = True
    visited_states[state_notation] = result
    return result


def print_path(piles: List[int], node: StateNode, level: int = 0, is_my_move: bool = False) -> None:
    row_index, number_of_takes = node.move

    piles[row_index] -= number_of_takes

    if number_of_takes == 0:
        print(f"Initial State: {piles}")
    else:
        move_repr = f"If {'I' if is_my_move else 'O'} takes {number_of_takes} sticks from row number {row_index + 1}"
        print(f"{'|    ' * level}{move_repr} (state after: {piles}), then I am winning = {node.is_winning}")

    for child in node.children:
        print_path(piles, child, level + 1, not is_my_move)

    piles[row_index] += number_of_takes


def search_for_winning_move(
        state: List[int],
        solution_dict: Dict[Tuple[int, ...], Tuple[int, int]]
) -> Tuple[int, int]:

    state_notation = tuple(sorted(state))

    ret = solution_dict[state_notation]

    row_number, number_of_takes = ret

    real_index = state.index(state_notation[row_number])

    return real_index, number_of_takes


class NimGameApp:
    def __init__(self, piles: List[int]):
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

    def __print_state(self) -> None:
        max_length = 2 * max(self.pile_counts) - 1
        for pile in self.pile_counts:
            row = " ".join(["*"] * pile)
            print(row.center(max_length))

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

    def print_game_tree(self):
        print_path(self.pile_counts, self.root_state)

    def play(self) -> None:
        if sum(self.pile_counts) == 0:
            print("You Won")
            return

        print("Current State: " + str(self.pile_counts))
        self.__print_state()

        try:
            winning_move = search_for_winning_move(self.pile_counts, self.solution_dict)
        except KeyError:
            print("We are losing")
            return

        row_number, number_of_takes = winning_move

        self.pile_counts[row_number] -= number_of_takes

        print(f"Next winning move: Takes {number_of_takes} sticks from row {row_number + 1}")

        print("After State: " + str(self.pile_counts))
        self.__print_state()

        print()
        print("Other move: ")

        other_row_number = int(input("\tOther row number: "))
        other_number_of_takes = int(input("\tOther number of takes: "))

        print(f"Other player has taken {other_number_of_takes} from row number {other_row_number}")

        self.pile_counts[other_row_number - 1] -= other_number_of_takes

        print("=" * 80)

        self.play()

if __name__ == '__main__':

    pile_counts = list(map(int, input("Rows: ").split(" ")))

    nim_app = NimGameApp(piles=pile_counts)

    nim_app.print_game_tree()

    nim_app.play()
