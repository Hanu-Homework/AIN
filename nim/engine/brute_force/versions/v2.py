def is_winning(pile1, pile2, is_my_turn=True, visited_states=dict()):
    state_notation = (pile1, pile2, is_my_turn)
    if state_notation in visited_states:
        return visited_states[state_notation]
    if pile1 + pile2 == 0:
        return not is_my_turn
    else:
        if is_my_turn:
            result = any(
                [is_winning(pile1 - i, pile2, not is_my_turn, visited_states) for i in range(1, pile1 + 1)]
                +
                [is_winning(pile1, pile2 - i, not is_my_turn, visited_states) for i in range(1, pile2 + 1)]
            )
        else:
            result = all(
                [is_winning(pile1 - i, pile2, not is_my_turn, visited_states) for i in range(1, pile1 + 1)]
                +
                [is_winning(pile1, pile2 - i, not is_my_turn, visited_states) for i in range(1, pile2 + 1)]
            )
        visited_states[state_notation] = result
        return result


if __name__ == '__main__':
    first_count = 1
    second_count = 3
    print(is_winning(first_count, second_count))
