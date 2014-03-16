# -*- coding: utf-8 -*-
"""Tests for the board interface.
"""
import pytest
from board import Board
from moves import Moves, InvalidMove
from player import Player

# Fixtures
@pytest.fixture
def joe():
    return Player('Joe', 'X')

@pytest.fixture
def mac():
    return Player('mac', 'O')

@pytest.fixture
def sample_move():
    return Moves.random()

@pytest.fixture
def sample_board(joe, mac):
    return Board(joe, mac)

# Tests
def test_move(sample_board, sample_move, joe):
    sample_board.turn(sample_move)
    assert sample_board.cell(sample_move) == joe.symbol

def test_moving_to_non_empty_square_is_illegal(sample_board, sample_move):
    with pytest.raises(InvalidMove):
        sample_board.turn(sample_move)
        sample_board.turn(sample_move)

def test_moving_switches_player(sample_board, sample_move):
    first_player = sample_board.current_player
    sample_board.turn(sample_move)
    assert first_player != sample_board.current_player

def test_sample_player_1_victory(joe, mac):
    board = Board(joe, mac)

    board.turn(Moves.top_left)
    board.turn(Moves.bottom_left)
    board.turn(Moves.top_right)
    board.turn(Moves.bottom_right)
    board.turn(Moves.top_middle)

    assert board.winner == joe
    assert board.is_game_over == True

def test_sample_player_2_victory(joe, mac):
    board = Board(joe, mac)

    board.turn(Moves.bottom_left)
    board.turn(Moves.top_left)
    board.turn(Moves.bottom_right)
    board.turn(Moves.top_right)
    board.turn(Moves.center_middle)
    board.turn(Moves.top_middle)

    assert board.winner == mac
    assert board.is_game_over == True

def test_sample_tie(joe, mac):
    board = Board(joe, mac)

    board.turn(Moves.top_left)
    board.turn(Moves.bottom_right)
    board.turn(Moves.top_right)
    board.turn(Moves.top_middle)
    board.turn(Moves.center_middle)
    board.turn(Moves.bottom_left)
    board.turn(Moves.bottom_middle)
    board.turn(Moves.center_right)
    board.turn(Moves.center_left)

    assert board.winner is None
    assert board.is_game_over == True
