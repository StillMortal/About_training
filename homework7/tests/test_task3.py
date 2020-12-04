from homework7.tasks.task3 import tic_tac_toe_checker


def test_when_x_is_the_winner():
    board = [["-", "-", "x"], ["-", "x", "o"], ["x", "o", "x"]]

    assert tic_tac_toe_checker(board) == "x wins!"


def test_when_o_is_the_winner():
    board = [["-", "-", "o"], ["-", "x", "o"], ["x", "o", "o"]]

    assert tic_tac_toe_checker(board) == "o wins!"


def test_when_the_game_ends_in_a_draw():
    board = [["x", "o", "o"], ["o", "o", "x"], ["x", "x", "o"]]

    assert tic_tac_toe_checker(board) == "draw!"


def test_when_game_is_unfinished():
    board = [["x", "x", "o"], ["o", "x", "o"], ["x", "o", "-"]]

    assert tic_tac_toe_checker(board) == "unfinished!"
