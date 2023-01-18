import random
import sys, os

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel
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
        self.lblBackground = self.findChild(QLabel, "lblBackground")
        self.lblPlayerPoints = [0, 0]
        self.lblPlayerPoints[0] = self.findChild(QLabel, "lblPlayer1Points")
        self.lblPlayerPoints[1] = self.findChild(QLabel, "lblPlayer2Points")
        self.lblp = [[0, 0, 0, 0], [0, 0, 0, 0]]
        for x in range(4):
            self.lblp[0][x] = self.findChild(QLabel, "lblp1_"+str(x+1))
            # self.lblp[0][x].hide()
            self.lblp[1][x] = self.findChild(QLabel, "lblp2_"+str(x+1))
            # self.lblp[1][x].hide()

        self.btnJoin = self.findChild(QPushButton, "btnSecondPlayer")

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

        self.vez = 0
        self.num1 = -1
        self.num2 = -1

        self.setStyle1 = ""
        self.setStyle2 = ""

        self.timer = QTimer()
        self.timer.timeout.connect(self.tempo)

        # self.btns[0].setStyleSheet("border-image: url(../archives/icons/blademooncard.png);")
        # RESPONSAVEL POR RANDOMIZAR
        self.reset()
        self.btnResets = self.findChild(QPushButton, "btnResets")
        self.btnResets.hide()
        self.btnReset = self.findChild(QPushButton, "btnReset")
        self.btnReset.clicked.connect(self.reset)
        # self.btnReset.hide()

        self.show()
    def reset(self):
        indexes1 = []
        indexes2 = []
        filePng = []

        for file in os.listdir('../archives/icons'):
            if file.__contains__("card.png"):
                filePng.append("(../archives/icons/" + file + ")")
        for file in os.listdir('../archives/icons'):
            if file.__contains__("card.png"):
                filePng.append("(../archives/icons/" + file + ")")

        for x in range(30):
            indexes1.append(x)
            indexes2.append(x)

        for x in range(30):
            escolha1 = random.choice(indexes1)
            escolha2 = random.choice(indexes2)
            while True:
                if self.btns[escolha1].styleSheet() != "":
                    self.btns[escolha1].setObjectName("border-image: url"+filePng[escolha2])
                    self.btns[escolha1].setStyleSheet("border-image: url(../archives/icons/backcards.png)")
                    break
            indexes1.remove(escolha1)
            indexes2.remove(escolha2)

    def num(self, num):
        if self.timer.isActive() or self.btns[num].objectName() == "border-image: url(../archives/icons/backcards.png)":
            print("ja foi meu ermao")
            return
        self.vez += 1
        if self.vez == 1:
            self.num1 = num
            self.setStyle1 = self.btns[num].objectName()
            self.btns[num].setStyleSheet(self.setStyle1)
            self.btns[num].setObjectName("border-image: url(../archives/icons/backcards.png)")
        elif self.vez == 2:
            self.num2 = num
            self.setStyle2 = self.btns[num].objectName()
            self.btns[num].setStyleSheet(self.setStyle2)
            self.btns[num].setObjectName("border-image: url(../archives/icons/backcards.png)")
            if self.btns[self.num1].styleSheet() != self.btns[self.num2].styleSheet():
                self.timer.start(1100)
            self.vez = 0

    def tempo(self):
        self.btns[self.num1].setObjectName(self.setStyle1)
        self.btns[self.num1].setStyleSheet("border-image: url(../archives/icons/backcards.png)")
        self.btns[self.num2].setObjectName(self.setStyle2)
        self.btns[self.num2].setStyleSheet("border-image: url(../archives/icons/backcards.png)")
        self.timer.stop()

    def points(self):
        for x in range(len(self.lblPlayerPoints)):
            if int(self.lblPlayerPoints[x].text()) > 10:
                self.lblp[x][3].show()
            if int(self.lblPlayerPoints[x].text()) > 6:
                self.lblp[x][2].show()
            if int(self.lblPlayerPoints[x].text()) > 4:
                self.lblp[x][1].show()
            if int(self.lblPlayerPoints[x].text()) >= 2:
                self.lblp[x][0].show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    memento = MementoGame()
    app.exec()
