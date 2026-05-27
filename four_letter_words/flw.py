from pathlib import Path
import check_inputs


file_path = Path('data\\four_letter_words.txt')

def run():
    """

    :return:
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file_object:
            # Perform file operations here
            the_file = file_object.read().splitlines()
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Something went wrong.")

    the_previous_word = ""

    while True:
        submitted_word = input("Enter a four letter word: ").upper()
        if submitted_word == "Q":
            break
        if not check_inputs.input_is_four_letters_long(submitted_word):
            print("That's not a four letter word. Try again or enter Q to quit.")
            continue
        if not check_inputs.input_is_in_file_list(the_file,submitted_word):
            print("That's not in Scrabble's list. Try again or enter Q to quit.")
            continue
        if not check_inputs.input_is_submitted_word_only_off_by_one_from_the_previous_word(the_previous_word,submitted_word):
            print("The submitted word is more than one letter different from the previous word. Try again or enter Q to quit.")
            continue
        the_previous_word = submitted_word
        print(submitted_word)

    print("Bye!")




if __name__ == '__main__':
    run()