import sys
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2.QtCore import*
from Tictactoe import*
from Algo import*

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #Récupération et application du thème
    myFile = open(".\darktheme.qss", "r")
    myQss = myFile.read()
    app.setStyleSheet(myQss)
    myFile.close()

    app.setApplicationName("TicTacToe")
    pix = QPixmap(".\tic.png")
    app.setWindowIcon(QIcon(pix))

    widget = Tictactoe()
    widget.build()
    widget.resize(900, 600)
    widget.show()

    sys.exit(app.exec_()) 