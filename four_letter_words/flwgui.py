from layout_ui import Ui_MainWindow
from check_inputs import Validator
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.submitted_word = None
        self.setupUi(self)
        self.validator = Validator()
        self.previous_word = ""
        self.pushButton.pressed.connect(self.handle_button_pressed)
        self.lineEdit.returnPressed.connect(self.handle_button_pressed)

    def handle_button_pressed(self):
        self.submitted_word = self.lineEdit.text()
        if self.validator.input_is_four_letters_long(self.submitted_word):
            if self.validator.input_is_in_file_list(self.submitted_word.upper()) :
                if self.validator.input_is_submitted_word_only_off_by_one_from_the_previous_word(self.submitted_word.upper(), self.previous_word):
                    self.listWidget.addItem(self.submitted_word.upper())
                    self.previous_word = self.submitted_word.upper()
                    self.lineEdit.clear()
                    self.listWidget.scrollToBottom()
                    return
                else:
                    QMessageBox.information(self, "Nope", "Your word is not only off by one letter from {self.previous_word}")
                    self.lineEdit.clear()
                    return
            else:
                QMessageBox.information(self, "Nope", "Your word is not in the word list! Take it up with Scrabble, if you don't like it.")
                self.lineEdit.clear()
                return
        else:
            QMessageBox.information(self, "Nope", "Your word is not four letters long!")
            self.lineEdit.clear()
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Calculon")

    window = MainWindow()
    window.show()
    app.exec()


