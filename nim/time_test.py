from time import time
from ain.nim.nim import is_winning

if __name__ == '__main__':
    start = time()
    print(is_winning(9, 9))
    end = time()
    print(end - start)