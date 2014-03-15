# -*- coding: utf-8 -*-
from player import Player
from moves import Moves, InvalidMove
from board import Board


if __name__ == "__main__":
    # Setup
    player_1 = Player('Joe', 'X')
    player_2 = Player('Mac', 'O')
    board = Board(player_1, player_2)

    # Main Loop
    while not board.is_game_over():
        board.paint()
        print board.pre_move_message()

        try:
            move = board.get_current_player().move()
            board.is_valid_move(move)
        except InvalidMove:
            continue

        board.turn(move)


    print board.print_eog_message()
