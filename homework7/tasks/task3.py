"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"

"""
from collections import Counter, defaultdict
from typing import List, Union


def checker(
    cells_to_check: Union[Counter, defaultdict], num_of_cells: int
) -> Union[str, None]:
    """Checks whether all passed cells are equal.

    Args:
        cells_to_check: Cells that need to be checked.
        num_of_cells: Number of cells.

    Returns:
        Winner if successful, None otherwise.

    """
    if "x" in cells_to_check and cells_to_check["x"] == num_of_cells:
        return "x wins!"
    elif "o" in cells_to_check and cells_to_check["o"] == num_of_cells:
        return "o wins!"


def main_diagonal(
    board: List[List], num_of_rows_on_board: int, num_of_columns_on_board: int
) -> Union[str, None]:
    """Checks the main diagonal on the board.

    Args:
        board: Tic-Tac-Toe 3x3 board.
        num_of_rows_on_board: Number of rows on the board.
        num_of_columns_on_board: Number of columns on the board.

    Returns:
        Winner is successful, None otherwise.

    """
    row, column = 0, 0
    values_in_the_cells = defaultdict(int)
    while row != num_of_rows_on_board and column != num_of_columns_on_board:
        values_in_the_cells[board[row][column]] += 1
        row += 1
        column += 1

    return checker(values_in_the_cells, min(row, column))


def side_diagonal(
    board: List[List], num_of_rows_on_board: int, num_of_columns_on_board: int
) -> Union[str, None]:
    """Checks the side diagonal on the board.

    Args:
        board: Tic-Tac-Toe 3x3 board.
        num_of_rows_on_board: Number of rows on the board.
        num_of_columns_on_board: Number of columns on the board.

    Returns:
        Winner is successful, None otherwise.

    """
    row, column = 0, num_of_columns_on_board - 1
    values_in_the_cells = defaultdict(int)
    while row != num_of_rows_on_board and column != -1:
        values_in_the_cells[board[row][column]] += 1
        row += 1
        column -= 1

    return checker(values_in_the_cells, min(row, num_of_columns_on_board))


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks if there are some winners.

    Args:
        board: Tic-Tac-Toe 3x3 board.

    Returns:
        Game outcome.

    """
    num_of_rows_on_board = len(board)
    num_of_columns_on_board = len(board[0])

    for row in range(num_of_rows_on_board):
        result = checker(Counter(board[row]), num_of_columns_on_board)
        if result:
            return result

    for column in range(num_of_columns_on_board):
        cells_in_the_column = [
            board[row][column] for row in range(num_of_rows_on_board)
        ]
        result = checker(Counter(cells_in_the_column), num_of_rows_on_board)
        if result:
            return result

    result = main_diagonal(board, num_of_rows_on_board, num_of_columns_on_board)
    if result:
        return result

    result = side_diagonal(board, num_of_rows_on_board, num_of_columns_on_board)
    if result:
        return result

    for row in range(num_of_rows_on_board):
        for column in range(num_of_columns_on_board):
            if board[row][column] == "-":
                return "unfinished!"

    return "draw!"
