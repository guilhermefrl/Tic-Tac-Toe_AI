"""
Tic Tac Toe
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
INF = math.inf


def initial_state():
    """
    Retorna o estado inicial do tabuleiro.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Retorna o jogador que tem a próxima jogada.
    """
    # Nota: o X joga primeiro

    # Contar o número de jogadas
    count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count +=1 

    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Retorna um array de todas as ações (i, j) possíveis no tabuleiro
    """

    possibleActions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.append((i, j))

    return possibleActions


def result(board, action):
    """
    Retorna o tabuleiro que resulta de fazer o movimento (i, j) no tabuleiro.
    """
    result = copy.deepcopy(board)

    # Caso não seja permitida essa ação
    if action not in actions(board):
        raise Exception("Invalid Action!")

    # Fazer a ação no tabuleiro
    result[action[0]][action[1]] = player(board)

    return result


def winner(board):
    """
    Retorna o vencedor do jogo, caso exista um.
    """
    # Verificar horizontalmente
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            if board[i][0] == X:
                return X
            else:
                return O

    # Verificar verticalmente
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY:
            if board[0][i] == X:
                return X
            else:
                return O

    # Verificar diagonalmete
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        if board[0][0] == X:
            return X
        else:
            return O

    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        if board[0][2] == X:
            return X
        else:
            return O

    # Caso ainda não exista um vencedor ou o jogo termine empatado
    return None


def terminal(board):
    """
    Retorna True caso o jogo esteja no estado terminal, caso contrário retorna False.
    """
    
    # Verificar se alguém ganhou o jogo
    if winner(board) == X or winner(board) == O:
        return True

    # Verificar se o tabuleiro está cheio
    if len(actions(board)) == 0:
        return True

    # Caso o jogo ainda esteja em progresso
    return False


def utility(board):
    """
    Retorna 1 se o X ganhar o jogo, -1 se o O ganhar o jogo, caso contrário 0.
    """

    # Esta função permite saber o resultado do jogo e assim inferir como deve jogar
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def alfabeta(board, alpha, beta):
    """
    Algoritmo Alpha-Beta Pruning
    """
    # Caso o jogo tenha terminado
    if terminal(board):
        return utility(board),None

    # Caso seja a vez da AI
    if player(board) == X:
        value = -INF
        best_action = -1
        for action in actions(board):
            v1 = alfabeta(result(board, action), alpha, beta)[0]
            if v1 > value:
                value = v1
                best_action = action
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        return value,best_action
    # Caso seja a vez do jogador
    else:
        value = INF
        best_action = 1
        for action in actions(board):
            v1 = alfabeta(result(board, action), alpha, beta)[0]
            if v1 < value:
                value = v1
                best_action = action
            beta = min(beta,value)
            if alpha >= beta:
                break
        return value,best_action