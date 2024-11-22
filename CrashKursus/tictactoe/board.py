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
    :param pieces: The pieces in the row. Defaults to all None
    :param size: The size of the row. Defaults to 3
    """

    def __init__(self, *pieces: Iterable[Piece | None], size: int = 3):
        self._size = size
        if not pieces:
            pieces = [None] * self._size
        if len(pieces) != self._size:
            raise ValueError(f"Row must contain exactly {size} elements")
        if not all(
            isinstance(piece, Piece) or piece is None for piece in pieces
        ):  # Only allow Pieces or None
            raise ValueError("Row must contain only Piece instances or None")
        self.pieces = list(pieces)

    def __setitem__(self, key: int, value: Piece | None):
        if not isinstance(value, Piece) and value is not None:
            raise ValueError("Row must contain only Piece instances or None")
        self.pieces[key] = value

    def __getitem__(self, key: int) -> Piece | None:
        return self.pieces[key]

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        return f"{self.pieces[0] or ' '} | {self.pieces[1] or ' '} | {self.pieces[2] or ' '}"


class Board:
    """
    A tic-tac-toe board.
    The board is a 3x3 grid of Rows.
    :param starting_player: The player who starts the game. Defaults to Piece.X
    :param size: The size of the board. Defaults to 3
    """

    def __init__(self, starting_player: Piece = Piece.X, size: int = 3):
        self._board = [
            Row(size=size) for _ in range(size)
        ]  # Label as private, don't allow direct access
        self.player_to_move = starting_player

    def __len__(self) -> int:
        return len(self._board)

    def __getitem__(self, key: int) -> Row:
        return self._board[key]

    def __setitem__(self, key: int, value: Row):
        if not isinstance(value, Row):
            raise ValueError("Board must contain only Row instances")
        self._board[key] = value

    def __str__(self) -> str:
        row_divider = "-" * (4 * len(self._board[0]) + 1) + "\n"
        content = row_divider
        for row_index, row in enumerate(self._board):
            content += "| "
            for col_index, cell in enumerate(row):
                cell_index = (
                    row_index * len(self._board) + col_index + 1
                )  # Add 1 to make it 1-indexed
                divider = (
                    " | "
                    if cell_index < 10 or cell
                    else "| " if cell_index < 99 else "|"
                )
                content += str(cell or cell_index) + divider
            content += "\n" + row_divider
        content = content[:-1]  # Remove trailing newline
        return content

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
        if not 0 <= index < len(self._board) * len(self._board[0]):
            raise IndexError("Index out of bounds")
        row, col = divmod(index, len(self._board))
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
        for i in range(len(self._board)):
            if len(set(self._board[i])) == 1 and self._board[i][0] is not None:  # Rows
                return self._board[i][0]
            if (
                len(set(row[i] for row in self._board)) == 1
                and self._board[0][i] is not None
            ):  # Columns
                return self._board[0][i]

        if self._board[0][0] is not None:  # Top Left->Bottom Right diagonal
            for i in range(len(self._board)):
                if self._board[i][i] != self._board[0][0]:
                    break
            else:
                return self._board[0][0]

        if self._board[-1][0] is None:  # Top Right-> Bottom Left diagonal
            for i in range(len(self._board)):
                if self._board[i][-1] != self._board[0][-1]:
                    break
            else:
                return self._board[0][-1]

        return None
