from typing import List, Tuple, Dict, Union

class StateNode:
    """A class that contains the information of one position for the Nim game

    Attributes:
        move (str): The move that has been made in the previous state.
        is_winning (:obj:`bool`, optional): Whether this position in winning or not.
        children (List[int]): All possible states that can be reached from this one
    """

    def __init__(self):
        self.move: Tuple[int, int] = (0, 0)
        self.is_winning: Union[bool, None] = None
        self.children: List[StateNode] = []

    def __repr__(self):
        return f"{self.move}"

    def to_json(self):
        return {
            "m": {
                "i": self.move[0],
                "n": self.move[1]
            },
            "w": 1 if self.is_winning else 0,
            "c": [child.to_json() for child in self.children]
        }

def solve(
        piles: List[int],
        current_state_node: StateNode,  # StateNode usage
        solution_dict: Dict[Tuple[int, ...], Tuple[int, int]],
        is_my_turn: bool=True,
        visited_states: Dict[Tuple[Tuple[int, ...], bool], bool]=None
) -> bool:
    """Solves the piles, creates a game tree and returns a dictionary containing the solution for each child state

    This is a brute force search algorithm applied with dynamic programming and memoization for the Nim game.

    After running this algorithm, the following input parameters will be modified:
        - current_state_node: this will contains the entire game tree, starting from the initial state as the root
        - solution_dict: this will contains all the solutions for all positions in the form of:
            key: state notation of the position, e.g: (1, 3, 5, 6): one stick in the first row, three sticks in the second...
            value: winning move as a tuple of (row_index, number_of_takes), e.g: (0, 2): take from the first row (0) two sticks (2)

    Args:
        piles ([int]): the current piles state
        current_state_node (StateNode): the current state node
        solution_dict (dict): the dictionary containing all current found solutions
        is_my_turn (bool): whether the next move is by this player or by the other player
        visited_states (dict): a dictionary that contain a state notation as key and a solution tuple as value

    Returns:
        bool: True is the current state is winning, False otherwise
    """

    # Default argument, only initialized this dict once at the beginning of the execution
    if visited_states is None:
        visited_states = dict()

    # BASE CASE:
    # Because the person who take the last stick will win,
    # the person who enter the state which has no sticks will lose
    # So, if there is nothing left
    if sum(piles) == 0:
        # Then if it is my turn,
        if is_my_turn:
            # then I've lost
            return False
        # Otherwise,
        else:
            # I've won
            return True

    # The tuple containing the representation for the current state
    # Example value: ((1, 3, 5, 6), False) => The pile counts for the
    # current position is 1, 3, 5, 6 and it is the other turn
    state_notation = (tuple(sorted(piles)), is_my_turn)

    # Check the current position whether it is calculated or not:

    # If the current position was determined in the previous steps
    if state_notation in visited_states:
        # Return it immediately, no more calculations
        return visited_states[state_notation]

    # Else, this position has never been met before, so calculate it with the following steps:

    # Initialize a boolean that holds the result:

    # If it is my turn, then if ANY of the next variations wins, I will win,
    # otherwise, I will lost with perfect play from both sides
    if is_my_turn:
        # Set the result for the current state to False, if ANY of the next paths win,
        # this will be changed to True (in the next step)
        result = False

    # Else if it is the other turn, then if ALL of the next variations is losing for the other player,
    # I will win, otherwise, I will lost with perfect play from both sides
    else:
        # Set the result for the current state to True, if ALL of the next paths are not winning,
        # this will be changed to False (in the next step)
        result = True

    is_result_determined = False

    # Brute forcing: Iterate through all possible next states from the current state
    for pile_index in range(len(piles)):

        if is_result_determined:
            break

        # In each turn, one player can take a minimum of 1 and a maximum of that pile count
        # So, the looping range is [1, current pile count + 1)
        for number_of_takes in range(1, piles[pile_index] + 1):

            if is_result_determined:
                break

            # Copy the current pile state to a new state array
            new_piles = piles.copy()
            # Remove from the current pile the current number of takes
            new_piles[pile_index] -= number_of_takes

            # With the new information for the next state, forms a new state node
            new_state_node = StateNode()
            new_state_node.move = (pile_index, number_of_takes)  # The move in order to reach this new state

            # Add this new state node as a child of the current state node
            current_state_node.children.append(new_state_node)

            # Recursive call on this new node to determine if this node is winning or not:
            #   - Invert the boolean is_my_turn
            #   - Solve with the child's piles array and the child's state node
            #   - Continue using the cache (solution_dict and visited_states) and updating them
            winning = solve(new_piles, new_state_node, solution_dict, not is_my_turn, visited_states)

            # Set the winning flag for this node
            new_state_node.is_winning = winning

            # If it is my turn and ONE OR MORE paths are winning
            if is_my_turn and winning:
                # Then I will definitely take that path, don't care about other path
                # So, the result for this state is winning for me, switch the result to True
                result = True
                is_result_determined = True

                # The representation for the current change
                pile_index_in_sorted_state = state_notation[0].index(piles[pile_index])
                solution_move = (pile_index_in_sorted_state, number_of_takes)

                # Save this to the solution dictionary
                #   - Key: the state that I'm having
                #   - Value: the tuple representing the move (row_index, number_of_takes)
                solution_dict[state_notation[0]] = solution_move

            # Else if it the other turn and ONE OR MORE paths are losing
            # (NOT ALL or the paths are winning for me)
            elif not is_my_turn and not winning:
                # Since the other player will play perfectly, they will choose this path
                # as it is winning for them. So, the result for this state is losing for me,
                # switch the result to False
                result = False
                is_result_determined = True

    # Save the result as a cache for future reuse (memoization)
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
