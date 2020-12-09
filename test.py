import random

def create_board():

    # Creating a 2D list to fill the '-' in the 7*7 matrix.
    board = [[" - "] * 7] * 7

    # Printing the numbers from 0 - 6
    print("     ", end="")
    for num1 in [0, 1, 2, 3, 4, 5, 6]:
        print(" {0} ".format(num1), end="")
    print()

    # Formatting the design of the board using '+' & '='.
    print("   +  =  =  =  =  =  =  =  +   ")

    # ------------ Placing the "General" in the random coloumn on Row 0 ------------

    # Generating a random number to decide the placement of "General" in Row 0.
    random_number = random.randint(0, 6)
    board[0][random_number] = ' G '

    # ------------ Placing the "Pawns" in all the coloumns in Row 1 ------------
    for number in range(7):
        board[1][number] = ' P '

    # ------------ Placing 2 "Bishops" in random columns on the last row ------------
    for x in range(2):
        random_placement_B = random.randint(0, 6)
        board[6][random_placement_B] = ' B '

    # ------------ Placing 2 "Rooks" in random columns on the last row ------------
    for y in range(2):
        random_placement_R = random.randint(0, 6)
        board[6][random_placement_R] = ' R '

    # Using the nested-loops to access and print each elements in the 2D list.
    number = 0
    for row in board:
        print(f" {number} | ", end="")
        for item in row:
            print(item, end="")
        print(f" | {number}")
        number = number + 1

    # Formatting the design of the board using '+' & '='.
    print("   +  =  =  =  =  =  =  =  +   ")

    # Printing the numbers from 0 - 6.
    print("     ", end="")
    for num2 in [0, 1, 2, 3, 4, 5, 6]:
        print(" {0} ".format(num2), end="")

    print(f"\n\nRandom Number = {random_number}")

if __name__ == '__main__':
    create_board()
