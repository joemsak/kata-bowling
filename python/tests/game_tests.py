from nose.tools import *
from game import Game

game = Game()

def test_all_ones_scores_twenty():
    assert_equal(20, game.getScore([1] * 20))

def test_spare_three_spare_one_gutters_scores_twenty_five():
    assert_equal(25, game.getScore([0, 10, 3, 7, 1] + [0] * 15))

def test_strike_then_ones_then_gutters_scores_fourteen():
    assert_equal(14, game.getScore([10, 1, 1] + [0] * 16))

def test_all_strikes_scores_three_hundred():
    assert_equal(300, game.getScore([10] * 12))

def test_complex_games():
    firstNineFrames = [10, 10, 10, 10, 5, 5, 6, 4, 10, 10, 10]
    assert_equal(261, game.getScore(firstNineFrames + [10, 10, 10]))
    assert_equal(236, game.getScore(firstNineFrames + [5, 5, 10]))
    assert_equal(224, game.getScore(firstNineFrames + [5, 4]))
