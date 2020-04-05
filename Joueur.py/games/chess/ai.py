# This is where you build your AI for the Chess game.

from joueur.base_ai import BaseAI
from games.chess.game_logic import *
from games.chess.game_ai import *
from games.chess.rules import *

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Chess. """

    @property
    def game(self) -> 'games.chess.game.Game':
        """games.chess.game.Game: The reference to the Game instance this AI is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.chess.player.Player':
        """games.chess.player.Player: The reference to the Player this AI controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control the player named this string.

        Returns:
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Chess Python Player" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player and game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic

        # example loading fen notation into a board
        fen = build_board_from_fen(self.game.fen, self.player.color)
        #print_board(fen)
        #print("print chess notation board:")
        chess_bd = build_chess_board()
        #print_board(chess_bd)
        print(self.player.color)

        #print("current board:")
        board = fen[:8]
        new_board = fen[:8]
        board[6][1] = '0'
        board[6][0] = '0'
        board[6][2] = '0'
        board[6][3] = '0'
        board[5][0] = 'P' # test knight enemy
        board[1][4] = '0' # test enemy king
        print_board(board)

        color = self.player.color
        """
        print("find all knight moves:")
        knightmoves = findall_knight_moves(board, color)
        print(knightmoves)
        print("find enemy knight moves:")
        knightmoves = findall_knight_moves(board, "white")
        print(knightmoves)
        
        print("find all bishop moves:")
        bishopmoves = findall_bishop_moves(board, color)
        print(bishopmoves)
        print("find all ememy bishop moves:")
        bishopmoves = findall_bishop_moves(board, "white")
        print(bishopmoves)
        
        print("find all castle moves:")
        castlemoves = findall_castle_moves(board, color)
        print(castlemoves)
        print("find all ememy moves:")
        castlemoves = findall_castle_moves(board, "white")
        print(castlemoves)
        
        print("find all queen moves:")
        queenmoves = findall_queen_moves(board, color)
        print(queenmoves)
        print("find all enemy queen moves:")
        queenmoves = findall_queen_moves(board, "white")
        print(queenmoves)
        
        print("find all pawn moves:")
        pawnmoves = findall_pawn_moves(board, color)
        print(pawnmoves)
        print("find all enemy pawn moves:")
        pawnmoves = findall_pawn_moves(board, "white")
        print(pawnmoves)
        

        # test adding all items together
        print("find ALL FRIEND moves:")
        friend_moves = generate_all_nonking_moves(board, color)
        print(friend_moves)
        print(len(friend_moves))

        # test generating all enemy moves
        print("find ALL ENEMY moves:")
        enemy_moves = generate_all_enemy_moves(board, color)
        print(enemy_moves)

        # test generating all king moves
        print("find generic king move:")
        king_moves = generate_king_moves([7, 4])
        print(king_moves)
        print(len(king_moves))
        """
        # generate the KING: this will generate all moves
        # if the king is in check, only moves that will save the king will be returned
        """
        print("find king moves:")
        king_moves = findall_king_moves(board, color)
        print(king_moves)
        print(len(king_moves))
        """

        # <<-- /Creer-Merge: start -->>

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def make_move(self) -> str:
        """This is called every time it is this AI.player's turn to make a move.
        """

        """
        Returns:
            str: A string in Universal Chess Inferface (UCI) or Standard Algebraic Notation (SAN) formatting for the move you want to make. If the move is invalid or not properly formatted you will lose the game.
        """
        # <<-- Creer-Merge: makeMove -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for makeMove
        return generate_random_move(self.game.fen, self.player.color)
        # <<-- /Creer-Merge: makeMove -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>
