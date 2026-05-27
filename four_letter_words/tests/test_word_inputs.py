"""
Tests of the input string
"""
import pytest

from check_inputs import (input_is_four_letters_long,
        input_is_submitted_word_only_off_by_one_from_the_previous_word, input_is_in_file_list)

@pytest.fixture
def the_mock_file() -> list:
    """
    Creates a mock dataframe containing four letters long words

    """
    return ['ACHE', 'BAKE', 'CAKE']

@pytest.fixture
def the_previous_word() -> str:
    '''
    A word that is four letters long, (probably) in the list and can be changed by one letter
    in each position to become another word in the list (CITE,BATE,BIKE, and BITS)
    :return:
    '''
    return 'BITE'


def test_input_is_in_word_list_pass(the_mock_file):
    """
    Compares a word known to be in the word list, expecting True
    """
    assert input_is_in_file_list(the_mock_file,'ACHE')

def test_input_is_in_word_list_fail(the_mock_file):
    """
    Compares a word known to not be in the word list, expecting False
    """
    assert input_is_in_file_list(the_mock_file,'AASD') is False

def test_input_is_four_letters_long_pass():
    """
    Checks if word that is four letters long passes the test
    """
    assert input_is_four_letters_long("pass")  is True

def test_input_is_four_letters_long_fail():
    """
    Checks if word that is not four letters long fails the test
    """
    assert input_is_four_letters_long("failed") is False

def test_compare_two_words_position_one_pass(the_previous_word):
    """
    Tests if a valid word differs from a previous word by one letter
    in the first position, like BITE and CITE

    """
    assert input_is_submitted_word_only_off_by_one_from_the_previous_word(
        the_previous_word,"CITE")

def test_compare_two_words_position_two_pass(the_previous_word):
    """
    Tests if a valid word differs from a previous word by one letter
    in the second position, like BITE and BATE

    """
    assert input_is_submitted_word_only_off_by_one_from_the_previous_word(the_previous_word,"BATE")

def test_compare_two_words_position_three_pass(the_previous_word):
    """
    Tests if a valid word differs from a previous word by one letter
    in the third position, like BITE and BIKE
    """
    assert input_is_submitted_word_only_off_by_one_from_the_previous_word(the_previous_word,"BIKE")

def test_compare_two_words_position_four_pass(the_previous_word):
    """
    Tests if a valid word differs from a previous word by one letter
    in the fourth position, like BITE and BITS
    """
    assert input_is_submitted_word_only_off_by_one_from_the_previous_word(the_previous_word,"BITS")


def test_input_is_submitted_word_only_off_by_one_from_the_previous_word_fail(the_previous_word):
    """
    Tests if a valid word differs from a previous word by more than one letter
    like BITE and FATE
    """
    assert input_is_submitted_word_only_off_by_one_from_the_previous_word(
        the_previous_word,"CUTE") is False
