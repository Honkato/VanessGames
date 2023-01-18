import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic


class LoseWin(QWidget):
    def __init__(self, condition):
        super(LoseWin, self).__init__()
        if condition:
            uic.loadUi("../archives/telasUI/winUIWidget.ui", self)
        else:
            uic.loadUi("../archives/telasUI/loseUIWidget.ui", self)

        self.btnOK = self.findChild(QPushButton, "btnOK")

        self.btnOK.clicked.connect(self.reset)

        self.show()

    def reset(self):
        # ui = game
        # ui.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = LoseWin(True)
    app.exec()
