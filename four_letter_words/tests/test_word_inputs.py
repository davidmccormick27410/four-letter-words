"""
Tests of the input string
"""
import pytest

from check_inputs import Validator


def test_input_is_in_word_list_pass():
    """
    Compares a word known to be in the word list, expecting True
    """
    submitted_word = "ACHE".upper()
    val = Validator()
    assert val.input_is_in_file_list(submitted_word)

def test_input_is_in_word_list_fail():
    """
    Compares a word known to not be in the word list, expecting False
    """
    val = Validator()
    assert val.input_is_in_file_list("AASD") is False

def test_input_is_four_letters_long_pass():
    """
    Checks if word that is four letters long passes the test
    """
    val = Validator()
    assert val.input_is_four_letters_long("pass")  is True

def test_input_is_four_letters_long_fail():
    """
    Checks if word that is not four letters long fails the test
    """
    submitted_word = "failed"
    val = Validator()
    assert val.input_is_four_letters_long(submitted_word) is False

def test_compare_two_words_position_one_pass():
    """
    Tests if a valid word differs from a previous word by one letter
    in the first position, like BITE and CITE

    """
    val = Validator()
    val.the_previous_word = "BITE"
    assert val.input_is_submitted_word_only_off_by_one_from_the_previous_word(
        "CITE")

def test_compare_two_words_position_two_pass():
    """
    Tests if a valid word differs from a previous word by one letter
    in the second position, like BITE and BATE

    """
    val = Validator()
    val.the_previous_word = "BITE"
    assert val.input_is_submitted_word_only_off_by_one_from_the_previous_word("BATE")

def test_compare_two_words_position_three_pass():
    """
    Tests if a valid word differs from a previous word by one letter
    in the third position, like BITE and BIKE
    """
    val = Validator()
    val.the_previous_word = "BITE"
    assert val.input_is_submitted_word_only_off_by_one_from_the_previous_word("BIKE")

def test_compare_two_words_position_four_pass():
    """
    Tests if a valid word differs from a previous word by one letter
    in the fourth position, like BITE and BITS
    """
    val = Validator()
    val.the_previous_word = "BITE"
    assert val.input_is_submitted_word_only_off_by_one_from_the_previous_word("BITS")


def test_input_is_submitted_word_only_off_by_one_from_the_previous_word_fail():
    """
    Tests if a valid word differs from a previous word by more than one letter
    like BITE and FATE
    """
    val = Validator()
    val.the_previous_word = "BITE"
    assert val.input_is_submitted_word_only_off_by_one_from_the_previous_word("CUTE") is False
