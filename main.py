# Global constants
import random

SIZE = 7


def replace(string, i, ch):
    return string[:i] + ch + string[i + 1:]


def create_board():
    board = ['-' * SIZE] * SIZE
    board[0] = replace(board[0], random.randrange(SIZE), 'G')
    board[1] = 'p' * SIZE
    r = random.sample(range(SIZE), 4)
    board[SIZE - 1] = replace(board[SIZE - 1], r[0], 'B')
    board[SIZE - 1] = replace(board[SIZE - 1], r[1], 'B')
    board[SIZE - 1] = replace(board[SIZE - 1], r[2], 'R')
    board[SIZE - 1] = replace(board[SIZE - 1], r[3], 'R')
    return board


def set_traps():
    trap_num = 0
    trap_board = [' ' * SIZE] * SIZE
    for j in range(2, SIZE-1):
        for i in range(SIZE):
            if random.random() <= 0.2:
                trap_board[j] = replace(trap_board[j], i, 'T')
                trap_num += 1
    print('This board has {} hidden traps.'.format(trap_num))
    return trap_board


def dis_traps(trap_board):
    lines = ['']*(SIZE+4)
    lines[0] = '  '
    for x in range(SIZE):
        lines[0] += str(x)
        lines[SIZE + 3] += str(x)
    lines[0] += '  '
    lines[1] = " +" + "=" * SIZE + "+ "
    for x in range(SIZE):
        lines[x+2] = "{}|".format(x) + trap_board[x] + "|{}".format(x)
    lines[SIZE+2] = " +" + "=" * SIZE + "+ "
    lines[SIZE+3] = lines[0]

    for line in lines:
        print(" ".join(line))


def display_board(board):
    lines = ['']*(SIZE+4)
    lines[0] = '  '

    for x in range(SIZE):
        lines[0] += str(x)
        lines[SIZE + 3] += str(x)

    for x in range(SIZE):
        lines[x+2] = "{}|".format(x) + board[x] + "|{}".format(x)

    lines[0] += '  '
    lines[1] = " +" + "=" * SIZE + "+ "
    lines[SIZE+2] = " +" + "=" * SIZE + "+ "
    lines[SIZE+3] = lines[0]

    for line in lines:
        print(" ".join(line))


def validate_moves(r, c, nr, nc, board):
    return True


def check_traps(r, c, nr, nc, tBoard):
    return False


def move_general(loc, board):
    for x in range(SIZE):
        if board[0][x] == 'G':
            board[0] = replace(board[0], x, ' ')
            board[0] = replace(board[0], loc, 'G')


def move_soldier():
    pass


def main():
    board = create_board()
    trap_board = set_traps()
    display_board(board)
    dis_traps(trap_board)


if __name__ == '__main__':
    main()
