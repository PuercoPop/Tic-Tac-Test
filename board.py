# -*- coding: utf-8 -*-
from sys import stdout
from itertools import cycle

class PlayerList(object):
    """Helper to keep track of player cycling.
    """
    def __init__(self, *args):
        self._players = cycle(args)
        self._current_player = args[0]

    @property
    def current_player(self, ):
        return self._current_player

    def next(self, ):
        self._current_player = self._players.next()
        return self._current_player


class Board(object):
    def __init__(self, player_1, player_2):
        """Takes both players as argument. Returns the board.
        """
        self.players = PlayerList(player_1, player_2, )
        self._board = [" "] * 9

    def __iter__(self, ):
        raise NotImplementedError

    def paint(self, ):
        print "-------------"
        for index, cell in enumerate(self._board): # TODO: enum on self
            if index % 3 == 0:
                stdout.write("| {cell} |".format(cell=cell))
            elif index % 3 == 1:
                stdout.write(" {cell} |".format(cell=cell))
            elif index % 3 == 2:
                print " {cell} |".format(cell=cell)
                print "-------------"

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
