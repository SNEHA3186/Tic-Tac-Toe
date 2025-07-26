def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            move = input(f"Player {current_player}, enter row and column (0-2) like '1 2': ")
            row, col = map(int, move.split())

            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break


            if is_full(board):
                print("It's a draw!")
                break

            # Switch player
            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")

# Run the game
tic_tac_toe()
