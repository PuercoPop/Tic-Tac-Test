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
def test_move(sample_board):
    board = sample_board
    move = Moves.top_right
    board.turn(move)
    assert board.cell(move) == joe.symbol

def test_moving_to_non_empty_square_is_illegal():
    with pytest.raises(InvalidMove):
        assert False

def test_moving_switches_player():
    assert False

def test_sample_player_1_victory():
    assert False

def test_sample_player_2_victory():
    assert False

def test_sample_tie():
    assert False
