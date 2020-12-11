def is_winning(pile1, pile2, is_my_turn=True):
    if pile1 + pile2 == 0:
        return not is_my_turn
    else:
        if is_my_turn:
            return any(
                [is_winning(pile1 - n, pile2, not is_my_turn) for n in range(1, pile1 + 1)]
                +
                [is_winning(pile1, pile2 - n, not is_my_turn) for n in range(1, pile2 + 1)]
            )
        else:
            return all(
                [is_winning(pile1 - n, pile2, not is_my_turn) for n in range(1, pile1 + 1)]
                +
                [is_winning(pile1, pile2 - n, not is_my_turn) for n in range(1, pile2 + 1)]
            )


if __name__ == '__main__':
    print(is_winning(3, 1))  # Output: True
