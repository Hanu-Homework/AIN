def is_winning(pile1, pile2, is_my_turn=True):
    if pile1 + pile2 == 1:
        return not is_my_turn
    else:
        if is_my_turn:
            return any(
                [is_winning(pile1 - i, pile2, not is_my_turn) for i in range(1, pile1 + 1 if pile2 > 0 else pile1)]
                +
                [is_winning(pile1, pile2 - i, not is_my_turn) for i in range(1, pile2 + 1 if pile1 > 0 else pile2)]
            )
        else:
            return all(
                [is_winning(pile1 - i, pile2, not is_my_turn) for i in range(1, pile1 + 1 if pile2 > 0 else pile1)]
                +
                [is_winning(pile1, pile2 - i, not is_my_turn) for i in range(1, pile2 + 1 if pile1 > 0 else pile2)]
            )


if __name__ == '__main__':
    first_count = 8
    second_count = 8
    print(is_winning(first_count, second_count))
