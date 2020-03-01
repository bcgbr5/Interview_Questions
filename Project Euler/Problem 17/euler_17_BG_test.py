# Project Euler Problem 17
# Tests : Brandon Greer
import pytest
import euler_17_BG as sut

def test_num_to_words():
    assert(sut.num_of_letters(1) == 3)

def test_sumation():
    assert(sut.sum_of_english_numbers(1, 5) == 19)
