import sys
from PySide2.QtWidgets import*
from PySide2.QtGui import*
from PySide2.QtCore import*
from Tictactoe import*
from Algo import*

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(app.font().setPointSize(50))

    widget = Tictactoe()
    widget.build()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_()) 