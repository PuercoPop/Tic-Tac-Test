# -*- coding: utf-8 -*-

class Board(object):
    def __init__(self, player_1, player_2):
        """Takes both players as argument. Returns the board.
        """
        raise NotImplementedError

    def __iter__(self, ):
        raise NotImplementedError

    def paint(self, ):
        raise NotImplementedError

    def __repr__(self, ):
        return self.paint()

    def cell(self, move):
        """Return the cell that the move references.
        ie. Moves.top_right -> return top_right cell.
        """

    def set_cell(self, move, value):
        """ # No setfable places.Fuck Python. Can't 'assign' functions.
        """
        raise NotImplementedError

    def turn(self, move):
        """Should raise InvalidMove if move illegal. ie. claiming a non empty
        square.."""
        raise NotImplementedError

    def is_valid_move(self, move):
        """Is move Legal in game? Assume valid input.
        """
        raise NotImplementedError

    def pre_move_message(self, ):
        raise NotImplementedError

    def end_of_game_message(self, move):
        raise NotImplementedError

    @property
    def current_player(self, ):
        """Return the current's player object.
        """
        raise NotImplementedError

    @property
    def is_game_over(self, move):
        raise NotImplementedError

    @property
    def winner(self, ):
        """Return the game's winner, None if no winner.
        """
        raise NotImplementedError
