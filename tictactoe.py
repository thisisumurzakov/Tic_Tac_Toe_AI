import copy
import math
import random

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
    sum_x = 0
    sum_o = 0
    for row in board:
        for i in row:
            if i == X:
                sum_x+=1
            elif i == O:
                sum_o +=1
    if sum_x > sum_o:
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i,j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
   # try:
    player_turn = player(board)
    #print(player_turn, type(player_turn))
    result_board = copy.deepcopy(board)
    #print(result_board)
    #print(action, 'result action')
    #print(type(action))
    result_board[action[0]][action[1]] = player_turn
    return result_board
    #except Exception:
     #   raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] == X \
            or board[1][0] == board[1][1] == board[1][2] == X \
            or board[2][0] == board[2][1] == board[2][2] == X \
            or board[0][0] == board[1][0] == board[2][0] == X \
            or board[0][1] == board[1][1] == board[2][1] == X \
            or board[0][2] == board[1][2] == board[2][2] == X \
            or board[0][0] == board[1][1] == board[2][2] == X \
            or board[2][0] == board[1][1] == board[0][2] == X:
        return X
    elif board[0][0] == board[0][1] == board[0][2] == O \
            or board[1][0] == board[1][1] == board[1][2] == O \
            or board[2][0] == board[2][1] == board[2][2] == O \
            or board[0][0] == board[1][0] == board[2][0] == O \
            or board[0][1] == board[1][1] == board[2][1] == O \
            or board[0][2] == board[1][2] == board[2][2] == O \
            or board[0][0] == board[1][1] == board[2][2] == O \
            or board[2][0] == board[1][1] == board[0][2] == O:
        return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for value in row:
            if value == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)
    else:
        if player(board) == X:
            return max_value1(board)
        else:
            return min_value1(board)

def max_value1(board):
    if len(actions(board)) == 9:
        return random.choice([(0,0),(0,2),(2,0),(2,2)])
    else:
        best_action = []
        allowed_actions = list(actions(board))
        for action in allowed_actions:
            global steps
            steps = 1
            best_action.append(min_value(result(board,action)))
        return allowed_actions[best_action.index(max(best_action))]

def min_value1(board):
    best_action = []
    allowed_actions = list(actions(board))
    for action in allowed_actions:
        global steps
        steps = 1
        best_action.append(max_value(result(board,action)))
    return allowed_actions[best_action.index(min(best_action))]


def max_value(board):
    global steps
    if terminal(board):
        return utility(board) / steps
    else:
        #if len(actions(board)) == 9:
        #    return random.choice([(0,0),(0,2),(2,0),(2,2),(1,1)])
        #else:
        steps+=1
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

def min_value(board):
    global steps
    if terminal(board):
        return utility(board) / steps
    else:
        steps+=1
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v