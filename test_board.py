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
    return Player('mac', 'X')

@pytest.fixture
def sample_board(joe, mac):
    return Board(joe, mac)

# Tests
def test_move(sample_board, joe):
    board = sample_board
    move = Moves.top_right
    board.turn(move)
    assert board.cell(move) == joe.symbol

def test_moving_to_non_empty_square_is_illegal(sample_board):
    with pytest.raises(InvalidMove):
        board = sample_board
        move = Moves.top_left
        board.turn(move)
        board.turn(move)

def test_moving_switches_player(sample_board, sample_move):
    first_player = sample_board.current_player
    sample_board.move(sample_move)
    assert first_player != sample_board.current_player

def test_sample_player_1_victory():
    assert False

def test_sample_player_2_victory():
    assert False

def test_sample_tie():
    assert False
