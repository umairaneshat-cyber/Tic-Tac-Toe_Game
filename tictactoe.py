"""Basic two-player Tic Tac Toe for the terminal."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]

def new_board():
    """Return an empty board: cells are numbered 1-9, stored as indexes 0-8."""
    return [" "] * 9


def print_board(board):
    print()
    for row in range(3):
        a, b, c = board[row * 3: row * 3 + 3]
        print(f" {a} | {b} | {c} ")
        if row < 2:
            print("---+---+---")
    print()


def get_move(board, player):
    """Ask the player for a cell (1-9) until a valid, empty one is chosen."""
    while True:
        choice = input(f"Player {player}, choose a cell (1-9): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue
        index = int(choice) - 1
        if board[index] != " ":
            print("That cell is already taken.")
            continue
        return index


def check_winner(board):
    """Return 'X' or 'O' if someone has won, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def play():
    board = new_board()
    player = "X"

    print("Tic Tac Toe - cells are numbered like this:")
    print_board([str(i) for i in range(1, 10)])

    while True:
        print_board(board)
        board[get_move(board, player)] = player
    
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            break
 
