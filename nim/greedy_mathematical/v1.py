from collections import defaultdict


class Node:
    pass


def to_binary_components(num: int):
    ret = []
    count = 0
    string = str(bin(num))[2:][::-1]
    for c in string:
        if c == '1':
            ret.append(2 ** count)
        count += 1

    return ret


def is_winning(rows: [int]):
    memo = defaultdict(int)

    for row in rows:
        binary = to_binary_components(row)

        for comp in binary:
            memo[comp] += 1

    print(memo)

    for key in memo.keys():
        memo[key] %= 2

        if memo[key] != 0:
            return True

    return False


def find_winning_move(rows: [int]):
    """
    Return the winning move from a nim position
    :param rows:
    :return: a tuple with the first as the row index to remove, second value as the number of sticks to remove,
    """

    memo = defaultdict(int)

    for row in rows:
        binary = to_binary_components(row)

        for comp in binary:
            memo[comp] += 1

    number_to_remove = 0

    for key in memo.keys():
        memo[key] %= 2

        if memo[key] != 0:
            number_to_remove += key

    for i, row in enumerate(rows):
        if row > number_to_remove:
            return i, number_to_remove

    return -1, -1


if __name__ == '__main__':
    print(is_winning([17, 3]))
    print(find_winning_move([17, 3]))
