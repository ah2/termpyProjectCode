# Global constants
import random

SIZE = 7
BOARD = []
TRAP_BOARD = []
TRAP_NUM = 0


def replace(s, i, ch):
    return s[:i] + ch + s[i + 1:]


def create_board():
    global BOARD
    BOARD = ['-' * SIZE] * SIZE
    BOARD[0] = replace(BOARD[0], random.randrange(SIZE), 'G')
    BOARD[1] = 'p' * SIZE
    r = random.sample(range(SIZE), 4)
    BOARD[SIZE - 1] = replace(BOARD[SIZE - 1], r[0], 'B')
    BOARD[SIZE - 1] = replace(BOARD[SIZE - 1], r[1], 'B')
    BOARD[SIZE - 1] = replace(BOARD[SIZE - 1], r[2], 'R')
    BOARD[SIZE - 1] = replace(BOARD[SIZE - 1], r[3], 'R')


def set_traps():
    global TRAP_NUM
    global TRAP_BOARD
    TRAP_BOARD = [' ' * SIZE] * SIZE
    for j in range(2, SIZE-1):
        for i in range(SIZE):
            if random.random() <= 0.2:
                TRAP_BOARD[j] = replace(TRAP_BOARD[j], i, 'T')
                TRAP_NUM += 1


def dis_traps():
    global TRAP_NUM
    lines = ['']*(SIZE+4)
    lines[0] = '  '
    for x in range(SIZE):
        lines[0] += str(x)
        lines[SIZE + 3] += str(x)
    lines[0] += '  '
    lines[1] = " +" + "=" * SIZE + "+ "
    for x in range(SIZE):
        lines[x+2] = "{}|".format(x) + TRAP_BOARD[x] + "|{}".format(x)
    lines[SIZE+2] = " +" + "=" * SIZE + "+ "
    lines[SIZE+3] = lines[0]

    for line in lines:
        print(" ".join(line))


def display_board():
    lines = ['']*(SIZE+4)
    lines[0] = '  '
    for x in range(SIZE):
        lines[0] += str(x)
        lines[SIZE + 3] += str(x)
    lines[0] += '  '
    lines[1] = " +" + "=" * SIZE + "+ "
    for x in range(SIZE):
        lines[x+2] = "{}|".format(x) + BOARD[x] + "|{}".format(x)
    lines[SIZE+2] = " +" + "=" * SIZE + "+ "
    lines[SIZE+3] = lines[0]

    for line in lines:
        print(" ".join(line))


def validate_moves():
    return True


def check_traps():
    return -1, -1


def move_general():
    pass


def move_soldier():
    pass


def main():
    create_board()
    display_board()
    set_traps()
    dis_traps()
    print('This board has {} hidden traps.'.format(TRAP_NUM))


if __name__ == '__main__':
    main()
