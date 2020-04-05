##############################################################
# Name: Hannah Reinbolt
# Date: 3-23-2020
# Class:CS 5400-101 - Intro to AI
# Assignment: Game Assignment #1 - Chess with Random Choice AI
# Note: This is the Game Logic file. Game rules and logic.
#############################################################

# libraries
#from games.chess.rules import * # importing this causes an issue


# build board from fen line
# takes: fen str
# returns: list of lists
def build_board_from_fen(board, color):
    # variables
    result = []
    tmp_board = []

    # split up the fen statement
    fen = board.split(" ")
    others = fen[1:]
    fen = fen[0]
    fen = fen.split("/")
    
    # check color for board orientation
    #if color == "white":
    #    fen.reverse() # reverse this if player is black, otherwise it is in the correct orientation for white

    # build board
    for line in fen:
        for item in line:

            # check if item is a number
            if item.isnumeric():
                for n in range(int(item)):
                    tmp_board.append("0")

            # add all letters
            else:
                tmp_board.append(item)

        # add to results and reset tmp board
        result.append(tmp_board)
        tmp_board = []

    # add on last fen details
    result.append(others)

    # return board: 2D list of lists
    return result


# build standard chess board
# takes: nothing
# returns: list of lists
def build_chess_board():
    # variables
    height = ["8", "7", "6", "5", "4", "3", "2", "1"]
    width = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board = []
    board_line = []

    # build board
    for h in height:
        for w in width:
            board_line.append(w+h)
        # fill main board and empty tmp
        board.append(board_line)
        board_line = []

    # return full board
    return board


# pretty print board
# takes: list of lists
# returns: nothing
def print_board(board):
    # variables
    tmp_line = ""
    
    # print board
    for line in board:
        for item in line:
            tmp_line = tmp_line + " " + str(item)

        # print and reset
        print(tmp_line)
        tmp_line = ""


# convert coordinates to UCI format
# takes: int, int
# returns: str
def coor_to_uci(height, width):

    # make standard chess board
    board = build_chess_board()

    # return uci location from chess board location
    return board[height][width]


# convert UCI format to coordinates
# takes: str, uci location
# returns: [int, int] or [height, width]
def uci_to_coor(location):

    # build chess board
    board = build_chess_board()

    # search through the board for the right str
    for height in range(0, len(board)):
        for width in range(0, len(board[height])):

            # check for correct element
            if board[height][width] == location:
                # return the correc coordinates
                return [height, width]

    # if was not found, then return empty list
    return []


# find enemy color
# takes: str, color
# returns: str, color
def find_enemy_color(color):

    # find opposite color
    if color == "white":
        return "black"
    else:
        return "white"


# find if peice is an enemy piece
# takes: TBD
# returns: TBD
def amienemy(piece, color):

    # check for black
    if color == "black":

        # check if friendly
        if piece.islower():
            return False
        else:
            return True

    # check for white
    else:

        # check if friendly
        if piece.isupper():
            return False
        else:
            return True


