#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ": return True
        if board[0][i] == board[1][i] == board[2][i] != " ": return True
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ": return True
    if board[0][2] == board[1][1] == board[2][0] != " ": return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board) and not is_full(board):
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                else:
                    print("Spot taken!")
            else:
                print("Coordinates must be 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print_board(board)
    if check_winner(board):
        # The winner is the player who just moved
        winner = "O" if player == "X" else "X"
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
