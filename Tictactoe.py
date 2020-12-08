import sys
from PySide2.QtWidgets import (QLabel, QPushButton,
                               QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QSizePolicy)
from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import *


class Tictactoe(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def build(self):
        # Build Main
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        # Build Left Panel
        self.leftWidget = QWidget()

        self.layoutLeft = QVBoxLayout()
        self.title = QLabel('TicTacToe')

        self.mainLayout.addWidget(self.leftWidget)
        self.leftWidget.setLayout(self.layoutLeft)
        self.layoutLeft.addWidget(self.title)

        self.layoutLeft.setAlignment(Qt.AlignTop)
        self.title.setStyleSheet("QLabel {font-size: 60px}")

        # Build Game Area
        self.widgetGameZone = QWidget()
        self.layoutGameZone = QGridLayout()

        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.button4 = QPushButton()
        self.button5 = QPushButton()
        self.button6 = QPushButton()
        self.button7 = QPushButton()
        self.button8 = QPushButton()
        self.button9 = QPushButton()

        self.mainLayout.addWidget(self.widgetGameZone)
        self.widgetGameZone.setLayout(self.layoutGameZone)

        self.layoutGameZone.addWidget(self.button1, 2, 0)
        self.layoutGameZone.addWidget(self.button2, 2, 1)
        self.layoutGameZone.addWidget(self.button3, 2, 2)
        self.layoutGameZone.addWidget(self.button4, 1, 0)
        self.layoutGameZone.addWidget(self.button5, 1, 1)
        self.layoutGameZone.addWidget(self.button6, 1, 2)
        self.layoutGameZone.addWidget(self.button7, 0, 0)
        self.layoutGameZone.addWidget(self.button8, 0, 1)
        self.layoutGameZone.addWidget(self.button9, 0, 2)

        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button1.setObjectName('1')
        self.button2.setObjectName('2')
        self.button3.setObjectName('3')
        self.button4.setObjectName('4')
        self.button5.setObjectName('5')
        self.button6.setObjectName('6')
        self.button7.setObjectName('7')
        self.button8.setObjectName('8')
        self.button9.setObjectName('9')

        self.button1.clicked.connect(self.newPlayerEntry)
        self.button2.clicked.connect(self.newPlayerEntry)
        self.button3.clicked.connect(self.newPlayerEntry)
        self.button4.clicked.connect(self.newPlayerEntry)
        self.button5.clicked.connect(self.newPlayerEntry)
        self.button6.clicked.connect(self.newPlayerEntry)
        self.button7.clicked.connect(self.newPlayerEntry)
        self.button8.clicked.connect(self.newPlayerEntry)
        self.button9.clicked.connect(self.newPlayerEntry)

    @Slot()
    def newPlayerEntry(self, myId):
        idObject = self.sender()
        print("You clicked " + idObject.objectName())

        self.button = self.findChild(QPushButton, idObject.objectName())
        self.button.setText("O")
        self.button.setEnabled(False)
