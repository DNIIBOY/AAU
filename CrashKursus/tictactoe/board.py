from typing import Iterable
from enum import Enum


class Piece(Enum):
    """
    An enum representing a piece in a tic-tac-toe game.
    """
    X = "X"
    O = "O"

    def __str__(self) -> str:
        return self.value


class Row:
    """
    A row on the board.
    Must contain 3 elements, each of which is either a Piece or None.
    :param pieces: The pieces in the row. Defaults to [None, None, None]
    """

    def __init__(self, *pieces: Iterable[Piece | None]):
        if not pieces:
            pieces = [None, None, None]
        if len(pieces) != 3:
            raise ValueError("Row must contain exactly 3 elements")
        if not all(isinstance(piece, Piece) or piece is None for piece in pieces):
            raise ValueError("Row must contain only Piece instances or None")
        self.pieces = list(pieces)

    def __setitem__(self, key: int, value: Piece | None):
        if not isinstance(value, Piece) and value is not None:
            raise ValueError("Row must contain only Piece instances or None")
        self.pieces[key] = value

    def __getitem__(self, key: int) -> Piece | None:
        return self.pieces[key]

    def __str__(self) -> str:
        return f"{self.pieces[0] or ' '} | {self.pieces[1] or ' '} | {self.pieces[2] or ' '}"


class Board:
    """
    A tic-tac-toe board.
    The board is a 3x3 grid of Rows.
    :param starting_player: The player who starts the game. Defaults to Piece.X
    """

    def __init__(self, starting_player: Piece = Piece.X):
        self._board = [Row() for _ in range(3)]  # Label as private, don't allow direct access
        self.player_to_move = starting_player

    def __getitem__(self, key: int) -> Row:
        return self._board[key]

    def __setitem__(self, key: int, value: Row):
        if not isinstance(value, Row):
            raise ValueError("Board must contain only Row instances")
        self._board[key] = value

    def __str__(self) -> str:
        return "\n".join(str(row) for row in self._board)

    def play(self, row: int, col: int) -> None:
        """
        Play a move on the board.
        :param row: The row to play the move in
        :param col: The column to play the move in
        :raises ValueError: If the cell is already occupied
        :return: None
        """
        if self._board[row][col] is not None:
            raise ValueError("Cell already occupied")
        self._board[row][col] = self.player_to_move
        self.player_to_move = Piece.X if self.player_to_move == Piece.O else Piece.O

    def play_index(self, index: int) -> None:
        """
        Play a move on the board, taking the index of a square.
        :param index of the square, must be between 0 and 8
        :raises IndexError: If the index is out of bounds
        :return: None
        """
        if not 0 <= index <= 8:
            raise IndexError("Index out of bounds")
        row, col = divmod(index, 3)
        self.play(row, col)

    def is_full(self) -> bool:
        """
        Check if the board is full.
        :return: True if the board is full, False otherwise
        """
        return all(all(cell is not None for cell in row) for row in self._board)

    def winner(self) -> Piece | None:
        """
        Check if there is a winner on the board.
        :return: The winning player, or None if there is no winner
        """
        for i in range(3):
            if self._board[i][0] == self._board[i][1] == self._board[i][2] and self._board[i][0] is not None:  # Rows
                return self._board[i][0]
            if self._board[0][i] == self._board[1][i] == self._board[2][i] and self._board[0][i] is not None:  # Columns
                return self._board[0][i]
        if self._board[0][0] == self._board[1][1] == self._board[2][2] and self._board[0][0] is not None:  # Left-right diagonal
            return self._board[0][0]
        if self._board[0][2] == self._board[1][1] == self._board[2][0] and self._board[0][2] is not None:  # Right-left diagonal
            return self._board[0][2]
        return None
