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
    sample_board.move(sample_move)
    assert first_player != sample_board.current_player

def test_sample_player_1_victory():
    assert False

def test_sample_player_2_victory():
    assert False

def test_sample_tie():
    assert False
