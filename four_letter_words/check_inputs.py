from os import path


class Validator():
    """
    Functions that validate the input

    1. Is the submitted word four letters long?
    2. Is the submitted word in the file list?
    3. Does the submitted word differ from the previous submitted word by only one letter?
    """
    def __init__(self):
        basedir = path.dirname(path.abspath(__file__))
        self.file_path = path.join(basedir, 'data\\four_letter_words.txt')
        self.word_list = ""
        self.the_previous_word = ""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file_object:
                # Perform file operations here
                self.word_list = file_object.read().splitlines()
        except FileNotFoundError:
            print("File not found.")
        except:
            print("Something went wrong.")

        self.the_previous_word = ""

    def input_is_four_letters_long(self,submitted_word: str) -> bool:
        """

        :param submitted_word:
        :return:
        """
        return len(submitted_word) == 4

    def input_is_in_file_list(self, submitted_word: str) -> bool:
        """
        :type submitted_word: str
        :param submitted_word:
        :return:
        """
        if submitted_word not in self.word_list:
            return False
        return True

    def input_is_submitted_word_only_off_by_one_from_the_previous_word(
            self,submitted_word):
        """
        :param submitted_word:
        :return:
        """
        if self.the_previous_word == "":
            return True
        matches = 0
        if submitted_word[0] == self.the_previous_word[0]:
            matches += 1
        if submitted_word[1] == self.the_previous_word[1]:
            matches += 1
        if submitted_word[2] == self.the_previous_word[2]:
            matches += 1
        if submitted_word[3] == self.the_previous_word[3]:
            matches += 1
        if matches == 3:
            return True
        return False

    def input_is_submitted_word_only_off_by_one_from_the_previous_word(
            self,submitted_word,previous_word):
        """
        :param submitted_word:
        :return:
        """
        if previous_word == "":
            return True
        matches = 0
        if submitted_word[0] == previous_word[0]:
            matches += 1
        if submitted_word[1] == previous_word[1]:
            matches += 1
        if submitted_word[2] == previous_word[2]:
            matches += 1
        if submitted_word[3] == previous_word[3]:
            matches += 1
        if matches == 3:
            return True
        return False
