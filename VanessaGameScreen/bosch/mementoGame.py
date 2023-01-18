import random
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QIcon, QMovie, QPixmap

class MementoGame(QWidget):
    def __init__(self):
        super(MementoGame, self).__init__()
        uic.loadUi("../archives/telasUI/mementomoriUIWidget.ui", self)
        self.btns = []
        for x in range(0,30):
            btn = self.findChild(QPushButton, "btn_"+str(x))
            self.btns.append(btn)

        self.btns[0].clicked.connect(lambda: self.num(0))
        self.btns[1].clicked.connect(lambda: self.num(1))
        self.btns[2].clicked.connect(lambda: self.num(2))
        self.btns[3].clicked.connect(lambda: self.num(3))
        self.btns[4].clicked.connect(lambda: self.num(4))
        self.btns[5].clicked.connect(lambda: self.num(5))
        self.btns[6].clicked.connect(lambda: self.num(6))
        self.btns[7].clicked.connect(lambda: self.num(7))
        self.btns[8].clicked.connect(lambda: self.num(8))
        self.btns[9].clicked.connect(lambda: self.num(9))
        self.btns[10].clicked.connect(lambda: self.num(10))
        self.btns[11].clicked.connect(lambda: self.num(11))
        self.btns[12].clicked.connect(lambda: self.num(12))
        self.btns[13].clicked.connect(lambda: self.num(13))
        self.btns[14].clicked.connect(lambda: self.num(14))
        self.btns[15].clicked.connect(lambda: self.num(15))
        self.btns[16].clicked.connect(lambda: self.num(16))
        self.btns[17].clicked.connect(lambda: self.num(17))
        self.btns[18].clicked.connect(lambda: self.num(18))
        self.btns[19].clicked.connect(lambda: self.num(19))
        self.btns[20].clicked.connect(lambda: self.num(20))
        self.btns[21].clicked.connect(lambda: self.num(21))
        self.btns[22].clicked.connect(lambda: self.num(22))
        self.btns[23].clicked.connect(lambda: self.num(23))
        self.btns[24].clicked.connect(lambda: self.num(24))
        self.btns[25].clicked.connect(lambda: self.num(25))
        self.btns[26].clicked.connect(lambda: self.num(26))
        self.btns[27].clicked.connect(lambda: self.num(27))
        self.btns[28].clicked.connect(lambda: self.num(28))
        self.btns[29].clicked.connect(lambda: self.num(29))

        # RESPONSAVEL POR RANDOMIZAR
        for x in range(15):
            for y in range(2):
                print(y)
                print(x)
        self.btnReset = self.findChild(QPushButton, "btnReset")
        self.btnReset.hide()

        self.show()
    def num(self, num):
        print(num)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    memento = MementoGame()
    app.exec()
