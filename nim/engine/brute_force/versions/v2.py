def is_winning(pile1, pile2, is_my_turn=True, memo=None):
    # Applied dynamic programming + memoization, reduced time complexity
    if memo is None:
        memo = {}
    elif (pile1, pile2, is_my_turn) in memo:
        return memo[(pile1, pile2, is_my_turn)]
    if pile1 + pile2 == 0:
        return is_my_turn
    else:
        if is_my_turn:
            result = any(
                [is_winning(pile1 - i, pile2, not is_my_turn, memo) for i in range(1, pile1 + 1)]
                +
                [is_winning(pile1, pile2 - i, not is_my_turn, memo) for i in range(1, pile2 + 1)]
            )
            memo[(pile1, pile2, is_my_turn)] = result
            return result
        else:
            result = all(
                [is_winning(pile1 - i, pile2, not is_my_turn, memo) for i in range(1, pile1 + 1)]
                +
                [is_winning(pile1, pile2 - i, not is_my_turn, memo) for i in range(1, pile2 + 1)]
            )
            memo[(pile1, pile2, is_my_turn)] = result
            return result


if __name__ == '__main__':
    first_count = 1
    second_count = 3
    print(is_winning(first_count, second_count))
