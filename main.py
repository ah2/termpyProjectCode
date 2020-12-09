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
    print('This board has {} hidden traps.'.format(trap_num))
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


def validate_moves(current_row, current_coloumn, new_row, new_coloumn, board):

    # Check if the soldier present at current location is 'B'.
    if board[current_row][current_coloumn] == ' B ' and (7 <= new_row >= 0) and (7 <= new_coloumn >= 0):
        if new_row == current_row + 1 and new_coloumn == current_coloumn + 1:
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True
        elif new_row == current_row - 1 and new_coloumn == current_coloumn - 1:
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True
        elif new_row == current_row - 1 and new_coloumn == current_coloumn + 1:
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True
        elif new_row == current_row + 1 and new_coloumn == current_coloumn - 1:
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True


def check_traps(r, c, nr, nc, tBoard):
    return False


def move_general(loc, board):
    for x in range(SIZE):
        if board[0][x] == 'G':
            board[0] = replace(board[0], x, ' ')
        board[0] = replace(board[0], loc, 'G')


def move_soldier(x, y, x2, y2, board, trap_board):
    tmp = ''
    if validate_moves(x, y, x2, y2, board):
        if check_traps(x, y, x2, y2, trap_board):
            print(f'There was a trap at [{0},{0}]. Your soldier dies!')
        else:
            tmp = board[y][x]
            board[y] = replace(board[y], x, '-')
            board[y2] = replace(board[y2], x2, tmp)
    else:
        print(f'Invalid move for {tmp}')


def main():
    board = create_board()
    trap_board = set_traps()
    display_board(board)
    # dis_traps(trap_board)

    while (True):
        print('To move your soldier enter it\'s current position <row,col>: ', end='')
        x1, y1 = map(int, input().split())
        print('Enter the new position <row,col>: ', end='')
        x2, y2 = map(int, input().split())
        move_soldier(x1, y1, x2, y2, board, trap_board)
        display_board(board)


if __name__ == '__main__':
    main()
