"""Tic Tac Toe: human (X) vs.  computer bot (O) using minimax."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]

HUMAN = "X"
BOT = "O"


def new_board():
    return [" "] * 9


def print_board(board):
    print()
    for row in range(3):
        a, b, c = board[row * 3: row * 3 + 3]
        print(f" {a} | {b} | {c} ")
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board):
    """Return 'X' or 'O' if someone has won, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return " " not in board


def minimax(board, is_bot_turn, depth=0):
    """
    Score a position from the bot's point of view.
    +10 - depth : bot wins (sooner is better)
    depth - 10  : human wins (later is better)
    0           : draw
    """
    winner = check_winner(board)
    if winner == BOT:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if is_full(board):
        return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = BOT if is_bot_turn else HUMAN
            scores.append(minimax(board, not is_bot_turn, depth + 1))
            board[i] = " "  # undo the move

    return max(scores) if is_bot_turn else min(scores)


def best_move(board):
    """Try every empty cell and pick the one with the highest minimax score."""
    best_score = float("-inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = BOT
            score = minimax(board, is_bot_turn=False, depth=1)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def get_human_move(board):
    while True:
        choice = input("Your move (1-9): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue
        index = int(choice) - 1
        if board[index] != " ":
            print("That cell is already taken.")
            continue
        return index


def play():
    board = new_board()
    human_first = input("Do you want to go first? (y/n): ").strip().lower() != "n"
    human_turn = human_first

    print(f"\nYou are {HUMAN}, the bot is {BOT}. Cells are numbered like this:")
    print_board([str(i) for i in range(1, 10)])

    while True:
        if human_turn:
            print_board(board)
            board[get_human_move(board)] = HUMAN
        else:
            board[best_move(board)] = BOT
            print("Bot has moved.")

        winner = check_winner(board)
        if winner or is_full(board):
            print_board(board)
            if winner == HUMAN:
                print("You win!")
            elif winner == BOT:
                print("The bot wins!")
            else:
                print("It's a draw!")
            break

        human_turn = not human_turn


if __name__ == "__main__":
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            break