from nose.tools import *
from game import Game

def test_all_gutters_scores_zero():
    game  = Game()
    rolls = [0] * 20
    score = game.score(rolls)
    assert_equal(0, score)

def test_all_ones_scores_twenty():
    game  = Game()
    rolls = [1] * 20
    score = game.score(rolls)
    assert_equal(20, score)
