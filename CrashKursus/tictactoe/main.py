#!/usr/bin/env python3
from board import Board


def main():
    board = Board()

    while not board.winner():
        print(f"Player {board.player_to_move}'s turn")
        print(board)
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        try:
            board.play(row, col)
        except ValueError as e:
            print(e)

    print(board)
    print(f"Player {board.winner()} wins!")


if __name__ == "__main__":
    main()
