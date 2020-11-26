# Global constants
import random

WIDTH = 7
HEIGHT = 7
board = []


def replace(s, i, ch):
    return s[:i] + ch + s[i + 1:]


def create_board():
    global board
    board = ['-' * WIDTH] * HEIGHT
    board[0] = replace(board[0], random.randrange(WIDTH), 'G')
    board[1] = 'p' * WIDTH
    r = random.sample(range(WIDTH), 4)
    board[HEIGHT-1] = replace(board[HEIGHT-1], r[0], 'B')
    board[HEIGHT-1] = replace(board[HEIGHT-1], r[1], 'B')
    board[HEIGHT-1] = replace(board[HEIGHT-1], r[2], 'R')
    board[HEIGHT-1] = replace(board[HEIGHT-1], r[3], 'R')


def set_traps():
    pass


def display_board():
    lines = ['']*(HEIGHT+4)

    lines[0] = '  '
    for x in range(WIDTH):
        lines[0] += str(x)
        lines[HEIGHT + 3] += str(x)
    lines[0] += '  '
    lines[1] = " +" + "=" * WIDTH + "+ "
    for x in range(HEIGHT):
        lines[x+2] = "{}|".format(x) + board[x] + "|{}".format(x)
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


if __name__ == '__main__':
    printboard()
