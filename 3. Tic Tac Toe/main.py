board = [" " for _ in range(9)]


def print_board(board):
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[0]} | {board[1]} | {board[2]}")


def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def check_tie(board):
    return " " not in board


current_player = "X"
game_over = False

print("Welcome to Tic Tac Toe!")

while not game_over:
    print_board(board)
    try:
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if move < 0 or move > 8:
            raise ValueError("Invalid number, please enter a number between 1-9.")

        if board[move] == " ":
            board[move] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif check_tie(board):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already occupied. Try again.")
    except ValueError:
        print("Invalid input, please enter a number between 1-9.")

print("Thanks for playing!")
