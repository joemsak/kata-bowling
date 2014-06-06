from nose.tools import *
from game import Game

def test_all_gutters_scores_zero():
    game  = Game()
    rolls = [0] * 20
    score = game.score(rolls)
    assert_equal(0, score)
