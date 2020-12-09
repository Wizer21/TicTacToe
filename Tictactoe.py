import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from Algo import *
import random

class Tictactoe(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.pixCircle = QPixmap(".\circle.png")
        self.pixCircle = self.pixCircle.scaled(100,100, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.pixCross = QPixmap(".\cross.png")
        self.pixCross = self.pixCross.scaled(100,100, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.playerScore = 0
        self.iaScore = 0
        self.nullScore = 0
        self.numberOfTurn = 0

    def build(self):
        # Build Main
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)

        # Build Left Panel
        self.leftWidget = QWidget()

        self.layoutLeft = QVBoxLayout()
        self.title = QLabel('TicTacToe')
        self.whoWon = QLabel()
        self.score = QLabel("Score:")
        self.playerScoreLabel = QLabel("You: 0")
        self.iaScoreLabel = QLabel("AI: 0")
        self.nullScoreLabel = QLabel("Null: 0")

        self.mainLayout.addWidget(self.leftWidget,0,0)
        self.leftWidget.setLayout(self.layoutLeft)
        self.layoutLeft.addWidget(self.title)
        self.layoutLeft.addWidget(self.whoWon)
        self.layoutLeft.addWidget(self.score)
        self.layoutLeft.addWidget(self.playerScoreLabel)
        self.layoutLeft.addWidget(self.iaScoreLabel)
        self.layoutLeft.addWidget(self.nullScoreLabel)

        # NEW
        self.newButton = QPushButton("New")
        self.mainLayout.addWidget(self.newButton,1,0)

        # Build Game Area
        self.widgetGameZone = QWidget()
        self.layoutGameZone = QGridLayout()

        self.button0 = QPushButton()
        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.button4 = QPushButton()
        self.button5 = QPushButton()
        self.button6 = QPushButton()
        self.button7 = QPushButton()
        self.button8 = QPushButton()

        self.mainLayout.addWidget(self.widgetGameZone,0,1,2,1)
        self.widgetGameZone.setLayout(self.layoutGameZone)

        self.layoutGameZone.addWidget(self.button0, 2, 0)
        self.layoutGameZone.addWidget(self.button1, 2, 1)
        self.layoutGameZone.addWidget(self.button2, 2, 2)
        self.layoutGameZone.addWidget(self.button3, 1, 0)
        self.layoutGameZone.addWidget(self.button4, 1, 1)
        self.layoutGameZone.addWidget(self.button5, 1, 2)
        self.layoutGameZone.addWidget(self.button6, 0, 0)
        self.layoutGameZone.addWidget(self.button7, 0, 1)
        self.layoutGameZone.addWidget(self.button8, 0, 2)

        self.button0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button0.setObjectName('0')
        self.button1.setObjectName('1')
        self.button2.setObjectName('2')
        self.button3.setObjectName('3')
        self.button4.setObjectName('4')
        self.button5.setObjectName('5')
        self.button6.setObjectName('6')
        self.button7.setObjectName('7')
        self.button8.setObjectName('8')

        self.button0.clicked.connect(self.newPlayerEntry)
        self.button1.clicked.connect(self.newPlayerEntry)
        self.button2.clicked.connect(self.newPlayerEntry)
        self.button3.clicked.connect(self.newPlayerEntry)
        self.button4.clicked.connect(self.newPlayerEntry)
        self.button5.clicked.connect(self.newPlayerEntry)
        self.button6.clicked.connect(self.newPlayerEntry)
        self.button7.clicked.connect(self.newPlayerEntry)
        self.button8.clicked.connect(self.newPlayerEntry)

        self.newButton.clicked.connect(self.relaodGame)

        self.buttonList = [self.button0, self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8]

        newGame()

        # Stylisation
        self.layoutLeft.setAlignment(Qt.AlignTop)
        self.leftWidget.setObjectName("leftborder")
        self.leftWidget.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)
        self.setContentsMargins(0,0,0,0)
        self.title.setObjectName("title")
        self.score.setObjectName("score")

    @Slot()
    def newPlayerEntry(self, myId):
        idObject = self.sender()
        print("You clicked " + idObject.objectName())

        self.newButtonClicked(1, idObject.objectName())

        self.newAtion(iniAlgo(idObject.objectName()))

    def newButtonClicked(self, whoInt, nameButton):
        self.newButton = self.findChild(QPushButton, str(nameButton))

        if whoInt == 1:
            self.newButton.setIcon(self.pixCircle)
        if whoInt == 2:
            self.newButton.setIcon(self.pixCross)

        self.newButton.setIconSize(QSize(120,120))
        self.newButton.blockSignals(True)
        self.newButton.setStyleSheet(self.getStyleDeadButton())

    def newAtion(self, val):
        self.numberOfTurn += 1

        isWin = int(val[0])
        if isWin == 1:
            self.whoWon.setText("You Won")
            self.playerScore += 1
            self.playerScoreLabel.setText("You: " + str(self.playerScore))
            self.freezButtons()
            return
        if isWin == 2:
            self.whoWon.setText("You Lose")
            self.iaScore += 1
            self.iaScoreLabel.setText("AI: " + str(self.iaScore))
            self.freezButtons()
        if val == "0null":
            self.whoWon.setText("Null")
            self.nullScore += 1
            self.nullScoreLabel.setText("Null: " + str(self.nullScore))
            self.freezButtons()
            return
        if self.numberOfTurn == 5:
            newPos = int(val[1]) * 3 + (int(val[2]))
            self.newButtonClicked(2, str(newPos))
            self.whoWon.setText("Null")
            self.nullScore += 1
            self.nullScoreLabel.setText("Null: " + str(self.nullScore))
            self.freezButtons()
            return

        newPos = int(val[1]) * 3 + (int(val[2]))

        self.newButtonClicked(2, str(newPos))

    def relaodGame(self):
        for i in self.buttonList:
            i.blockSignals(False)
            i.setIcon(QPixmap(""))
            i.setStyleSheet(self.getStyleNewButton())

        self.whoWon.setText("")
        self.numberOfTurn = 0
        newGame()
        dice = random.randint(0, 1)
        if dice == 1:
            self.newAtion(iniAlgo(str(9)))

        myFile = open(".\darktheme.qss", "r")
        myQss = myFile.read()
        self.setStyleSheet(myQss)
        myFile.close()

    def freezButtons(self):
        for i in self.buttonList:
            i.blockSignals(True)
            i.setStyleSheet(self.getStyleDeadButton())

    def getStyleDeadButton(self):
        return """
QPushButton {
  background-color: #091833;
  padding: 5px;
  border: 0px solid transparent;
}
QPushButton::hover {
}
QPushButton::pressed {
  background-color: #ff2b36;
  padding: 5px;
  border: 0px solid transparent;
}"""

    def getStyleNewButton(self):
        return """
        QPushButton {
  background-color: #091833;
  padding: 5px;
  border: 0px solid red;
}
QPushButton::hover {
  border: 1px solid #ff2b36;
}
QPushButton::pressed {
  background-color: #ff2b36;
  color: #292929;
  padding: 5px;
  border: 0px solid transparent;
}"""