from typing import List

a = [['x', 'o', 'x'],
     ['x', 'o', 'x'],
     ['o', 'x', 'x']]


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    >>> line = [['o', 'x', 'o'],['x', 'o', 'o'],['o', 'o', 'x']]
    >>> print(tic_tac_toe_checker(line))
    o wins!
    >>> line = [['-', '-', 'o'],['-', 'x', 'o'],['x', 'o', 'x']]
    >>> print(tic_tac_toe_checker(line))
    unfinished!
    >>> line = [['o', 'x', 'o'],['o', 'x', 'o'],['x', 'o', 'x']]
    >>> print(tic_tac_toe_checker(line))
    draw!

    :param board:
    :return:
    """
    unfinished = False
    for i in enumerate(board): # (0, [x,0,x])
        if '-' in i[1]: # check for "-"
            unfinished = True
        if len(set(i[1])) == 1 and i[1][0] != '-': #We take a unique value in the list. If the dimension of the set is >1, then there is no winner in the row.
            return f"{i[1][0]} wins!" # If =1 , then the winner is determined.
        elif board[0][i[0]] == board[1][i[0]] == board[2][i[0]] != '-':
            return f"{i[1][i[0]]} wins!"
        if board[0][0] == board[1][1] == board[2][2] \
                or board[2][0] == board[1][1] == board[0][2]:
            return f"{board[1][1]} wins!"
    if unfinished: #if there is no winner
        return "unfinished!"
    else:
        return "draw!"

