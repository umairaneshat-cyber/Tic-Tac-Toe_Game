"""Tic Tac Toe: human (X) vs.  computer bot (O) using minimax."""
def print_board(board):
    print()
    for i in range(3):
        print(" " + " | ".join(board[i * 3:i * 3 + 3]))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def minimax(board, computer_turn):
    winner = check_winner(board)

    if winner == "O":
        return -1

    if winner == "X":
        return 1

    if " " not in board:
        return 0

    if computer_turn:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score

    else:
        best_score = float("-inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score


def computer_move(board):
    best_score = float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score < best_score:
                best_score = score
                best_move = i

    return best_move


def play_game():
    board = [" "] * 9

    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The computer is O.")
    print("Enter a position from 1 to 9.")
    print()

    print("Position guide:")
    print_board(["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"])

    while True:
        # User's turn
        try:
            position = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position < 0 or position >= 9 or board[position] != " ":
            print("Invalid move. Try again.")
            continue

        board[position] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("Congratulations! You win!")
            break

        if " " not in board:
            print("It's a draw!")
            break

        # Computer's turn
        move = computer_move(board)
        board[move] = "O"

        print("Computer chooses position", move + 1)
        print_board(board)

        if check_winner(board) == "O":
            print("Computer wins!")
            break

        if " " not in board:
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
