# Global constants
import random

SIZE = 7


def replace(string, i, ch):
    return string[:i] + ch + string[i + 1:]


def compare(i, j):
    if i < j:
        return 1
    if i > j:
        return -1
    return 0


def create_board():
    board = ['-' * SIZE] * SIZE
    board[0] = replace(board[0], random.randrange(SIZE), 'G')
    board[1] = 'P' * SIZE
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
        if abs(c_row - c_col) == abs(n_row - n_col) \
                or c_row + c_col == c_row + n_col:
            return True

    return False


def check_traps(c_row, c_col, n_row, n_col, trap_board):
    # check if we reached destination:
    if c_row == n_row and c_col == n_col:
        return False, c_row, c_col

    # check if there is a trap in current location:
    if trap_board[c_row][c_col] == 'T':
        return True, c_row, c_col

    # get delta movement in X-axis
    x = compare(c_col, n_col)

    # get delta movement in Y-axis
    y = compare(c_row, n_row)

    # recursively call with one unit of movement in X, Y axis
    return check_traps(c_row + y, c_col + x, n_row, n_col, trap_board)


def move_general(board):
    # find and remove G from the  first row
    for col in range(SIZE):
        if board[0][col] == 'G':
            board[0] = replace(board[0], col, '-')

    # get random values until we find an empty location
    while True:
        n_col = random.randrange(SIZE)
        if board[0][n_col] == '-':
            board[0] = replace(board[0], n_col, 'G')
            break


def move_soldier(c_row, c_col, n_row, n_col, board, trap_board):

    score_dict = {'-': 0, 'P': 2, 'G': 1000}
    tmp = board[c_row][c_col]

    # check if move is valid
    if validate_moves(c_row, c_col, n_row, n_col, board):
        # check recursively for traps
        trap, t_col, t_row = check_traps(c_row, c_col, n_row, n_col, trap_board)

        # updating the board with a T and returning score
        if trap:
            board[c_row] = replace(board[c_row], c_col, '-')
            board[t_row] = replace(board[t_row], t_col, 'T')
            print(f'There was a trap at [{t_col},{t_row}]. Your soldier dies!')
            return -1

        # no trap found, check if soldier captured
        else:
            e_sol = board[n_row][n_col]
            board[c_row] = replace(board[c_row], c_col, '-')
            board[n_row] = replace(board[n_row], n_col, tmp)
            return score_dict[e_sol]

    else:
        print(f'Invalid move for {tmp}')
        return 0


def main():
    print('Game starts now >>')

    # initialize board, traps, number of soldiers and score
    board = create_board()
    trap_board = set_traps()
    score = 0
    num_sol = 4

    # display_board(board)
    dis_traps(trap_board)

    while num_sol > 0 and score < 1000:
        # display board and score
        display_board(board)
        print(f'Your score: {score}')

        try:
            # get user input
            print('To move your soldier enter it\'s current position <row,col>: ', end='')
            y1, x1 = map(int, input().split(','))
            print('Enter the new position <row,col>: ', end='')
            y2, x2 = map(int, input().split(','))

            # calc score and number of soldiers left:
            tmp_score = move_soldier(y1, x1, y2, x2, board, trap_board)
            score += tmp_score
            if tmp_score == -1:
                num_sol -= 1

            # moving general for next run
            move_general(board)

        except ValueError:
            print('Invalid input')

    # game finish
    # check if lost
    if num_sol < 1:
        print('you lose!')
        return

    # check if won
    if score >= 1000:
        print(f'you Win! Final score: {score}')
        return


if __name__ == '__main__':
    main()
