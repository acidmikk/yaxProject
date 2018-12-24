import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainw import MainWindow
from calc import Calc


class Osnv(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calc)

    def calc(self):
        exc = Cal
        exc.show()


class Cal(QMainWindow, Calc):
    def __init__(self):
        super().__init__()
        self.setupUic(self)


app = QApplication(sys.argv)
ex = Osnv()
ex.show()
sys.exit(app.exec_())