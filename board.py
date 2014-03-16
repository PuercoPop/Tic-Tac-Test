# -*- coding: utf-8 -*-
from sys import stdout
from itertools import cycle
from moves import Moves, InvalidMove

class PlayerList(object):
    """Helper to keep track of player cycling.
    """
    def __init__(self, *args):
        self._players = cycle(args)
        self.next()
        # Because one can't use list comprehension of cycles, save a dict from
        # player symbols to player object to be able to look a player by
        # symbol.
        self._from_symbols = dict()
        for player in args:
            self._from_symbols[player.symbol] = player

    @property
    def current_player(self, ):
        return self._current_player

    def next(self, ):
        self._current_player = self._players.next()
        return self._current_player

    def player_from_symbol(self, symbol):
        # Explicit better than implicit ;)
        return self._from_symbols.get(symbol, None)


class Board(object):
    def __init__(self, player_1, player_2):
        """Takes both players as argument. Returns the board.
        """
        self._players = PlayerList(player_1, player_2, )
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
        return self._board[move - 1]

    def set_cell(self, move, value):
        """ # No setfable places.Fuck Python. Can't 'assign' functions.
        """
        self._board[move - 1] = value
        return self._board[move - 1]

    def turn(self, move):
        """Should raise InvalidMove if move illegal. ie. claiming a non empty
        square.."""
        if self.is_valid_move(move):
            self.set_cell(move, self.current_player.symbol)
            self._players.next()
        else:
            raise InvalidMove

    def is_valid_move(self, move):
        """Is move Legal in game? Assume valid input.
        """
        return " " == self.cell(move)

    def pre_move_message(self, ):
        return "{name} make your move".format(name=self.current_player.name)

    def end_of_game_message(self, ):
        if self.winner:
            return "Congratulations {name}, You Won!".format(
                name=self.winner.name)
        else:
            return "As expected, game was tie. *yawn*"

    @property
    def current_player(self, ):
        """Return the current's player object.
        """
        return self._players.current_player

    @property
    def is_game_over(self, ):
        return (self.winner is not None  or
                len([cell for cell in self._board if cell == " "]) == 0)

    @property
    def winner(self, ):
        """Return the game's winner, None if no winner.
        """
        if self.cell(Moves.top_right) == self.cell(Moves.top_middle) == self.cell(Moves.top_left):
            return self._players.player_from_symbol(self.cell(Moves.top_right))
        elif self.cell(Moves.center_right) == self.cell(Moves.center_middle) == self.cell(Moves.center_left):
            return self._players.player_from_symbol(self.cell(Moves.center_left))
        elif self.cell(Moves.bottom_right) == self.cell(Moves.bottom_middle) == self.cell(Moves.bottom_left):
            return self._players.player_from_symbol(self.cell(Moves.bottom_left))
        elif self.cell(Moves.top_right) == self.cell(Moves.center_right) == self.cell(Moves.bottom_right):
            return self._players.player_from_symbol(self.cell(Moves.bottom_right))
        elif self.cell(Moves.top_middle) == self.cell(Moves.center_middle) == self.cell(Moves.bottom_middle):
            return self._players.player_from_symbol(self.cell(Moves.bottom_middle))
        elif self.cell(Moves.top_left) == self.cell(Moves.center_left) == self.cell(Moves.bottom_left):
            return self._players.player_from_symbol(self.cell(Moves.bottom_left))
        elif self.cell(Moves.top_right) == self.cell(Moves.center_middle) == self.cell(Moves.bottom_left):
            return self._players.player_from_symbol(self.cell(Moves.bottom_left))
        elif self.cell(Moves.top_left) == self.cell(Moves.center_middle) == self.cell(Moves.bottom_right):
            return self._players.player_from_symbol(self.cell(Moves.bottom_right))
        else:
            return None
