from StateNode import StateNode


def solve(piles: [int], current_state_node: StateNode, solution_dict: dict, is_my_turn=True, memo=None):
    # Solvable for multiple piles

    if memo is None:
        memo = {}

    state_notation = (tuple(sorted(piles)), is_my_turn)

    if state_notation in memo:
        return memo[state_notation]

    sum_piles = sum(piles)

    if sum_piles == 0:
        return is_my_turn
    else:
        if is_my_turn:
            result = False
        else:
            result = True

        for i in range(len(piles)):
            for number_of_takes in range(1, piles[i] + 1):

                new_piles = piles.copy()
                new_piles[i] -= number_of_takes

                new_state_node = StateNode()

                move = (i, number_of_takes)

                new_state_node.move = move

                current_state_node.children.append(new_state_node)

                winning = solve(new_piles, new_state_node, solution_dict, not is_my_turn, memo)

                new_state_node.is_winning = winning

                if is_my_turn and winning:
                    solution_dict[state_notation[0]] = move
                    result = True
                elif not is_my_turn and not winning:
                    result = False

        memo[state_notation] = result

        return result


def print_path(piles: [int], node: StateNode, level: int = 0, is_my_move=False):
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


def search_for_winning_move(state: [int], solution_dict) -> tuple:
    state_notation = tuple(sorted(state))

    ret = solution_dict[state_notation]

    row_number, number_of_takes = ret

    real_index = state.index(state_notation[row_number])

    return real_index, number_of_takes


def print_state(piles: [int]):
    max_length = 2 * max(piles) - 1
    for pile in piles:
        row = " ".join(["*"] * pile)
        print(row.center(max_length))


def play(piles: [int], solution_dict: dict):
    if sum(piles) == 0:
        print("You Won")
        return

    print("Current State: " + str(piles))
    print_state(piles)

    try:
        winning_move = search_for_winning_move(piles, solution_dict)
    except KeyError:
        print("We are losing")
        return

    row_number, number_of_takes = winning_move

    piles[row_number] -= number_of_takes

    print(f"Next winning move: Takes {number_of_takes} sticks from row {row_number + 1}")

    print("After State: " + str(piles))
    print_state(piles)

    print()
    print("Other move: ")

    other_row_number = int(input("\tOther row number: "))
    other_number_of_takes = int(input("\tOther number of takes: "))

    print(f"Other player has taken {other_number_of_takes} from row number {other_row_number}")

    piles[other_row_number - 1] -= other_number_of_takes

    print("=" * 80)

    play(piles, solution_dict)


if __name__ == '__main__':
    root_state = StateNode()

    solution = dict()

    pile_counts = list(map(int, input("Rows: ").split(" ")))

    print("Winning: " + str(solve(pile_counts, root_state, solution)))

    # print_path(pile_counts, root_state)

    print("=" * 80)

    # print(solution)

    play(pile_counts, solution)
