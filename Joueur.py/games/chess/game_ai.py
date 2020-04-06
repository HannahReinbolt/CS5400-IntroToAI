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


# generate random nonking move for AI
# takes: fen board (str) and color (str)
# returns: str
def generate_random_nonking_move(fen, color):
    # generate fen board
    board = build_board_from_fen(fen, color)[:8]

    # generate moves
    moves = generate_all_nonking_moves(board, color)

    # random choice by piece
    # make list of pieces
    p_lst = [i for i in moves]

    # pick random piece
    rand_p = random.choice(p_lst)

    # pick random move
    move_lst = [i for i in moves[rand_p]]
    rand_move = random.choice(move_lst)

    # return random move and print random moves from that piece
    print(str(rand_p)+": "+str(moves[rand_p]))
    return rand_move


# genreate random move for AI
# takes: fen board (str) and color (str)
# returns: str
def generate_random_move(fen, color):
    # variables
    board = build_board_from_fen(fen, color)[:8]

    # generate moves
    moves = findall_king_moves(board, color)

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
