# -*- coding: utf-8 -*-
from random import choice

class InvalidMove(Exception):
    pass


class Moves(object):
    top_right = 1
    top_middle = 2
    top_left = 3
    center_right = 4
    center_middle = 5
    center_left = 6
    bottom_right = 7
    bottom_middle = 8
    bottom_left = 9

    def __iter__(self, ):
        """Nom nom boilerplate.
        """
        return self

    def next(self, ):
        for move in Moves.all():
            yield move
        else:
            raise StopIteration

    @classmethod
    def random(cls, ):
        return choice(cls.all())

    @classmethod
    def all(cls, ):
        return filter( lambda x: x not in [cls.all, cls.random, cls.next],
                       [getattr(cls, move)
                        for move in dir(cls)
                        if not(move[:2] == "__"  == move[-2:]) ])
