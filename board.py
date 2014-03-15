# -*- coding: utf-8 -*-

class Board(object):
    def __iter__(self, ):
        raise NotImplementedError

    def paint(self, ):
        raise NotImplementedError

    def __repr__(self, ):
        return self.paint()

    def turn(self, move):
        raise NotImplementedError

    def is_valid_move(self, move):
        """Is move Legal in game? Assume valid input.
        """

    def pre_move_message(self, ):
        raise NotImplementedError

    def end_of_game_message(self, move):
        raise NotImplementedError

    def current_player(self, ):
        """Return the current's player object.
        """
        raise NotImplementedError

    def is_game_over(self, move):
        raise NotImplementedError

    def winner(self, ):
        """Return the game's winner, None if no winner.
        """
        raise NotImplementedError
