##############################################################
# Name: Hannah Reinbolt
# Date: 3-23-2020
# Class:CS 5400-101 - Intro to AI
# Assignment: Game Assignment #1 - Chess with Random Choice AI
# Note: This is the Game Logic file. Game rules and logic.
#############################################################

# libraries
import random
from games.chess.rules import *
from games.chess.game_logic import *


# genreate random move for AI
# takes: fen board (str) and color (str)
# returns: str
def generate_random_move(fen, color):
    # variables
    board = build_board_from_fen(fen, color)[:8]

    # gerante all moves
    moves = generate_all_moves(board, color) 

    # random choice by piece
    # make list of pieces
    p_lst = [i for i in moves]

    # pick random pieces
    rand_p = random.choice(p_lst)

    # pick random move
    move_lst = [i for i in moves[rand_p]]
    rand_move = random.choice(move_lst)

    # return random move and print random moves from that piece
    print(str(rand_p)+": "+str(moves[rand_p]))
    return rand_move


# score move made on board based on what value piece it took or destination it moved to
# takes: board (list of lists), move (str) and history of values (dict of str)
# returns: dictionary of lists
def score_move(board, move, history):
    # variables
    p_value = {'P': 1, 'p': 1, 'B': 3, 'b': 3, 'N': 3, 'n': 3, 'R': 5, 'r': 5, 'Q': 9, 'q': 9, 'K': 10, 'k': 10}
    move_coor = uci_to_coor(move[2:4])
    p_taken = board[move_coor[0]][move_coor[1]]

    # calculate what value move it made
    if p_taken != '0':
        # should be in p_value so no need to check
        new_val = p_value[p_taken]

        # add to history
        if new_val not in history:
            history[new_val] = []
        # add
        history[new_val] = history[new_val] + [move]
        
    # otherwise the value is at 0 and is rated at 0
    else:

        # check if it is in history
        if 0 not in history:
            history[0] = []
        # add
        history[0] = history[0] + [move]

    # return history
    return history
    

# score all moves on entire board for one player
# takes: board (list of lists) and moves dictionary of lists
# returns: dictionary of lists
def score_board(board, moves):
    # variables
    scored = {}

    # score each move
    for piece in moves:
        for move in moves[piece]:

            # get score
            scored = score_move(board, move, scored)

    # return scored board
    return scored


# find minimum value move from current turn played by player
# takes: moves (dictionary of lists)
# returns: str
def find_min(moves):
    # variables
    result = ""

    # find min from moves
    min_move = min(moves.keys())
    small = moves[min_move]

    # if there are more than one move, then chose a random min value
    if len(small) > 1:
        result = random.choice(small)

    # otherwise return single move
    else:
        result = small

    return result


# find maximum value move from current turn played by player
# takes: moves (dictionary of lists)
# returns: str
def find_max(moves):
    # variables
    result = ""
    
    # find max from moves
    max_move = max(moves.keys())
    big = moves[max_move]

    # if there is more than one move, then chose a random max move
    if len(big) > 1:
        result = random.choice(big)

    # otherwise return single move
    else:
        result = big

    return result


