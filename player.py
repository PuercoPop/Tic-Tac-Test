# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def move(self, board):
        """Should ensure a valid input.
        """
        raise NotImplementedError

    def __repr__(self,):
        return self.name
