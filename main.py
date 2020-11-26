# Global constants
import random

WIDTH = 7
HEIGHT = 7
BOARD = []
TRAP = []
TRAPN = 0


def replace(s, i, ch):
    return s[:i] + ch + s[i + 1:]


def create_board():
    global BOARD
    BOARD = ['-' * WIDTH] * HEIGHT
    BOARD[0] = replace(BOARD[0], random.randrange(WIDTH), 'G')
    BOARD[1] = 'p' * WIDTH
    r = random.sample(range(WIDTH), 4)
    BOARD[HEIGHT - 1] = replace(BOARD[HEIGHT - 1], r[0], 'B')
    BOARD[HEIGHT - 1] = replace(BOARD[HEIGHT - 1], r[1], 'B')
    BOARD[HEIGHT - 1] = replace(BOARD[HEIGHT - 1], r[2], 'R')
    BOARD[HEIGHT - 1] = replace(BOARD[HEIGHT - 1], r[3], 'R')


def set_traps():
    global TRAPN
    global TRAP
    TRAP = [' ' * WIDTH] * HEIGHT
    for j in range(2, HEIGHT-1):
        for i in range(WIDTH):
            if random.random() <= 0.2:
                TRAP[j] = replace(TRAP[j], i, 'T')
                TRAPN += TRAPN+1


def dis_traps():
    global TRAPN
    lines = ['']*(HEIGHT+4)
    lines[0] = '  '
    for x in range(WIDTH):
        lines[0] += str(x)
        lines[HEIGHT + 3] += str(x)
    lines[0] += '  '
    lines[1] = " +" + "=" * WIDTH + "+ "
    for x in range(HEIGHT):
        lines[x+2] = "{}|".format(x) + TRAP[x] + "|{}".format(x)
    lines[HEIGHT+2] = " +" + "=" * WIDTH + "+ "
    lines[HEIGHT+3] = '  '
    for x in range(WIDTH):
        lines[HEIGHT+3] += str(x)
    lines[HEIGHT+3] += lines[HEIGHT+3] + '  '

    for line in lines:
        print(" ".join(line))


def display_board():
    lines = ['']*(HEIGHT+4)
    lines[0] = '  '
    for x in range(WIDTH):
        lines[0] += str(x)
        lines[HEIGHT + 3] += str(x)
    lines[0] += '  '
    lines[1] = " +" + "=" * WIDTH + "+ "
    for x in range(HEIGHT):
        lines[x+2] = "{}|".format(x) + BOARD[x] + "|{}".format(x)
    lines[HEIGHT+2] = " +" + "=" * WIDTH + "+ "
    lines[HEIGHT+3] = '  '
    for x in range(WIDTH):
        lines[HEIGHT+3] += str(x)
    lines[HEIGHT+3] += lines[HEIGHT+3] + '  '

    for line in lines:
        print(" ".join(line))


def validate_moves():
    pass


def check_traps():
    pass


def move_general():
    pass


def move_soldier():
    pass


def main():
    pass


def printboard():
    create_board()
    display_board()
    set_traps()
    dis_traps()
    print('This board has {} hidden traps.'.format(TRAPN))


if __name__ == '__main__':
    printboard()
