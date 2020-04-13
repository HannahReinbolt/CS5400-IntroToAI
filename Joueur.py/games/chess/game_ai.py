##############################################################
# Name: Hannah Reinbolt
# Date: 4-12-2020
# Class:CS 5400-101 - Intro to AI
# Assignment: Game Assignment #2 - Iterative Deepening Depth Limited Minimax AI
# Note: This file contains all the AI functionality.
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
    #print(str(rand_p)+": "+str(moves[rand_p]))
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


# find score of move in the completed scoring dictionary
# takes: scores (dictionary of lists) and move (str)
# returns: list (str, int)
def find_move_score(scores, move):

    # find score
    for score in scores:
        for item in scores[score]:

            # check for the move
            if item == move:
                return score

    # else return empty 
    return 0


# find minimum or maximum value move from current turn played by player
# takes: moves (dictionary of lists) and choice (str)
# returns: str
def find_min_or_max(moves, choice):
    # variables
    move = ""
    score = 0

    # chose max or min
    if choice == "max":
        score = max(moves)
    else:
        score = min(moves)

    # find list from moves
    move_lst = moves[score]

    # if there are more than one move, then chose a random min value
    if len(move_lst) > 1:
        move = random.choice(move_lst)

    # otherwise return single move
    else:
        move = move_lst[0]

    return [move, score]


# scoring heuristic, calculates how each move is scored against parents and other levels
####################################
# How this works:
####################################
# subtract enemy points, add friend points. 
# All children are compared and best child is computed and compared with parent. 
# curr_score = current default parent score
# next_score = best child score of all levels and children below parent
# High enemy capture points = less desireable, High friend capture points = more desireable
# odd level = enemy level, even level = friend level

# takes: level number (int), current score (int) and next score (int)
# returns: int
def score_heuristic(level, curr_score, next_score):
    # variables
    odd = amiodd(level)
    final = 0

    # subtract the enemy points and add the friend points
    # the higher the friend points, the more desireable of a move it is
    if odd == True:
        final = next_score - curr_score
    else:
        final = next_score + curr_score

    return final


# find best minimax move by level recursivly
# takes: board (list of lists), color (str), pastmove (str), score (int), level (int) and stop (int)
# returns: list (str, int)
def minimax_by_level_recursive(board, color, pastmove, score, level, stop):
    # variables
    history = {}
    result_move = []
    enemy_color = find_enemy_color(color)
    final_score = 0

    # check level
    if level == stop:
        return [pastmove, score]

    # if not hit level yet then generate next level
    all_moves = generate_all_moves(board, color)
    scores = score_board(board, all_moves)

    # calculate next level for each move
    for piece in all_moves:
        for move in all_moves[piece]:

            # build board for this move
            nextboard = build_board_from_move(board, move)
            move_score = find_move_score(scores, move)

            # find new score from deeper levels
            new_score = minimax_by_level_recursive(nextboard, enemy_color, move, move_score, level+1, stop)[1]
            
            # calculate new score based on future levels
            final_score = score_heuristic(level, move_score, new_score)

            # add this to a dictionary
            if final_score not in history:
                history[final_score] = []

            # add
            history[final_score] = history[final_score] + [move]

    # if level is odd then return max score, if even then return min
    islevelodd = amiodd(level)

    # find min or max valued move at this level
    if islevelodd == True:
        result_move = find_min_or_max(history, "max")
    else:
        result_move = find_min_or_max(history, "min")

    # return best move and score for this level
    return result_move

   
# iterative deepening depth limited minimax move generation
# takes: fen board (str) and color (str)
# returns: str
def iddl_minimax(fen, color):
    # variables
    board = build_board_from_fen(fen, color)[:8]

    # start recursive function to find iterative deep move
    final_move = minimax_by_level_recursive(board, color, '', 0, 0, 2)

    # return best move
    return final_move[0]


