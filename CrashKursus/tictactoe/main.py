#!/usr/bin/env python3
from board import Board


def main():
    board = Board()

    while not board.winner():
        print(f"Player {board.player_to_move}'s turn")
        print(board)
        cell = int(input("Enter cell (1-9): ")) - 1  # Convert to 0-indexed
        try:
            board.play_index(cell)
        except (IndexError, ValueError) as e:
            print(e)

    print(board)
    print(f"Player {board.winner()} wins!")


if __name__ == "__main__":
    main()
