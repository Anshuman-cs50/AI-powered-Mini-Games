"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
            continue

    if x_count == o_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Invalid action")
    
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")
    
    result_Board = copy.deepcopy(board)
    result_Board[action[0]][action[1]] = player(board)

    return result_Board


def winner(board):
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if won, the game has ended
    if winner(board):
        return True

    # if no one won, check for EMPTY in each row
    for i in range(3):
        if EMPTY in board[i]:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w:
        if w == X:
            return 1
        elif w == O:
            return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if winner(board):
        return None
    
    optimal_action = None

    p = player(board)
    if p == X:
        v = -math.inf
        for action in actions(board):
            min_val = Min_value(result(board, action))
            if min_val > v:
                v = min_val
                optimal_action = action
    else:
        v = math.inf
        for action in actions(board):
            max_val = Max_value(result(board, action))
            if max_val < v:
                v = max_val
                optimal_action = action

    return optimal_action


def Max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, Min_value(result(board, action)))
    return v

def Min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, Max_value(result(board, action)))
    return v
