# -*- coding: utf-8 -*-
from moves import Moves

class Player(object):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def move(self, board):
        """Should ensure a valid input.
        """
        while True:
            message = """
            """.format()
            input = raw_input(message)
            if input in Moves:
                return input

    def __repr__(self,):
        return self.name
