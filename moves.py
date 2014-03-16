# -*- coding: utf-8 -*-
from random import choice

class InvalidMove(Exception):
    pass


class Moves(object):
    top_right = 1
    top_middle = 2
    top_left = 3
    middle_right = 4
    middle_middle = 5
    middle_left = 6
    bottom_right = 7
    bottom_middle = 8
    bottom_left = 9

    @classmethod
    def random(cls):
        return choice([move for move in dir(cls)
                       if not(move[:2] == "__"  == move[-2:]) ])
