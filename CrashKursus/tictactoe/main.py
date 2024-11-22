#!/usr/bin/env python3
from board import Board


def main():
    board = Board(size=3)

    while not (board.winner() or board.is_full()):
        print(f"Player {board.player_to_move}'s turn")
        print(board)
        try:
            cell = (
                int(input(f"Enter cell (1-{len(board)*len(board[0])}): ")) - 1
            )  # Convert to 0-indexed
            board.play_index(cell)
        except (IndexError, ValueError) as e:
            print(e)

    print(board)
    if board.winner():
        print(f"Player {board.winner()} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit(0)
