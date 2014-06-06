from nose.tools import *
from game import Game

game = Game()

def test_all_gutters_scores_zero():
    assert_equal(0, game.score([0] * 20))

def test_all_ones_scores_twenty():
    assert_equal(20, game.score([1] * 20))
