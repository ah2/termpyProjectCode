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
    for j in range(2, SIZE - 1):
        for i in range(SIZE):
            if random.random() <= 0.2:
                trap_board[j] = replace(trap_board[j], i, 'T')
                trap_num += 1
    print(f'\nThis board has {trap_num} hidden traps.\n')
    return trap_board


def dis_traps(trap_board):
    lines = [''] * (SIZE + 4)
    lines[0] = '  '
    for x in range(SIZE):
        lines[0] += str(x)
        lines[SIZE + 3] += str(x)
    lines[0] += '  '
    lines[1] = " +" + "=" * SIZE + "+ "
    for x in range(SIZE):
        lines[x + 2] = "{}|".format(x) + trap_board[x] + "|{}".format(x)
    lines[SIZE + 2] = " +" + "=" * SIZE + "+ "
    lines[SIZE + 3] = lines[0]

    for line in lines:
        print(" ".join(line))


def display_board(board):
    lines = [''] * (SIZE + 4)
    lines[0] = '  '

    for x in range(SIZE):
        lines[0] += str(x)
        lines[SIZE + 3] += str(x)

    for x in range(SIZE):
        lines[x + 2] = "{}|".format(x) + board[x] + "|{}".format(x)

    lines[0] += '  '
    lines[1] = " +" + "=" * SIZE + "+ "
    lines[SIZE + 2] = " +" + "=" * SIZE + "+ "
    lines[SIZE + 3] = lines[0]

    for line in lines:
        print(" ".join(line))


def validate_moves(c_row, c_col, n_row, n_col, board):
    # check if any value is outside the board:
    for x in (c_row, c_col, n_row, n_col):
        if x < 0 or x > SIZE:
            return False

    # check if destination if occupied
    if board[n_row][n_col] in ('R', 'B'):
        return False

    # check if move is valid for Rock:
    if board[c_row][c_col] == 'R':
        if c_row == n_row or c_col == n_col:
            return True

    # check if move is valid for Bishop:
    if board[c_row][c_col] == 'B':
        if abs(c_row - c_col) == abs(n_row - n_col) or c_row + c_col == c_row + n_col:
            return True

    return False


def check_traps(c_row, c_col, n_row, n_col, trap_board):
    return False, 0, 0


def move_general(n_col, board):
    for col in range(SIZE):
        if board[0][col] == 'G':
            board[0] = replace(board[0], col, ' ')
        board[0] = replace(board[0], n_col, 'G')


def move_soldier(row, col, n_row, n_col, board, trap_board):
    tmp = board[row][col]
    if validate_moves(row, col, n_row, n_col, board):
        trap, t_col, t_row = check_traps(row, col, n_row, n_col, trap_board)
        if trap:
            board[row] = replace(board[row], col, '-')
            board[n_row] = replace(board[n_row], n_col, 'T')
            print(f'There was a trap at [{t_col},{t_row}]. Your soldier dies!')
        else:
            board[row] = replace(board[row], col, '-')
            board[n_row] = replace(board[n_row], n_col, tmp)
    else:
        print(f'Invalid move for {tmp}')


def main():
    print('Game starts now >>')
    board = create_board()
    trap_board = set_traps()
    score = 0

    display_board(board)
    # dis_traps(trap_board)

    while True:
        try:
            print('To move your soldier enter it\'s current position <row,col>: ', end='')
            y1, x1 = map(int, input().split(','))
            print('Enter the new position <row,col>: ', end='')
            y2, x2 = map(int, input().split(','))

            move_soldier(y1, x1, y2, x2, board, trap_board)
            display_board(board)
            print(f'Your score: {score}')

        except (ValueError, IndexError):
            print('Invalid input')


if __name__ == '__main__':
    main()
