"""
Functions that validate the input

1. Is the submitted word four letters long?
2. Is the submitted word in the file list?
3. Does the submitted word differ from the previous submitted word by only one letter?
"""

def input_is_in_file_list(word_list,submitted_word: str) -> bool:
    """
    :type submitted_word: str
    :param word_list: a dataframe
    :param submitted_word: 
    :return: 
    """
    if submitted_word not in word_list:
        return False
    return True

def input_is_four_letters_long(submitted_word: str) -> bool:
    """
    
    :param submitted_word: 
    :return: 
    """
    return len(submitted_word) == 4

def input_is_submitted_word_only_off_by_one_from_the_previous_word(
        the_previous_word,submitted_word):
    """
    :param the_previous_word:
    :param submitted_word: 
    :return: 
    """