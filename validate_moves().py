def validate_moves(current_row, current_coloumn, new_row, new_coloumn, board):

    # Check if the soldier present at current location is 'B' and the new location is not outside the board.
    if board[current_row][current_coloumn] == ' B ' and (SIZE <= new_row >= 0) and (SIZE <= new_coloumn >= 0):

        # Moving diagonally right-down.
        if new_row == current_row + 1 and new_coloumn == current_coloumn + 1:
            # Check if there is a soldier at the new location.
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True

        # Moving diagonally left-up.
        elif new_row == current_row - 1 and new_coloumn == current_coloumn - 1:
            # Check if there is a soldier at the new location.
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True

        # Moving diagonally right-up.
        elif new_row == current_row - 1 and new_coloumn == current_coloumn + 1:
            # Check if there is a soldier at the new location.
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True

        # Moving diagonally left-down.
        elif new_row == current_row + 1 and new_coloumn == current_coloumn - 1:
            # Check if there is a soldier at the new location.
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True

    # Check if the soldier present at current location is 'R' and the new location is not outside the board.
    elif board[current_row][current_coloumn] == ' R ' and (SIZE <= new_row >= 0) and (SIZE <= new_coloumn >= 0):

        # Check if the new location is in the same row or same coloumn.
        if new_row == current_row or new_coloumn == current_coloumn:
            # Check if there is a soldier at the new location.
            if board[new_row][new_coloumn] == ' B ' or ' R ':
                return False
            else
                return True
