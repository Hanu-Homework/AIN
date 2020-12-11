def is_winning(piles, is_my_turn=True):
    if sum(piles) == 0:
        return not is_my_turn
    result = not is_my_turn
    for pile_index in range(len(piles)):
        for number_of_takes in range(1, piles[pile_index] + 1):
            new_piles = piles.copy()
            new_piles[pile_index] -= number_of_takes
            winning = is_winning(new_piles, not is_my_turn)
            if is_my_turn and winning:
                result = True
            elif not is_my_turn and not winning:
                result = False
    return result

if __name__ == '__main__':
    pile_counts = list(map(int, input("Rows: ").split(" ")))
    print(is_winning(piles=pile_counts))
