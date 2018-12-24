import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainw import MainWindow
from calc import Calc
ftom


class Osnv(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super(Osnv, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calc)
        self.callcalc = Cal(self)

    def calc(self):
        self.callcalc.show()

    def foto(self):
        self.callfoto.show(self)


class Cal(QMainWindow, Calc):
    def __init__(self, parent=None):
        super(Cal, self).__init__(parent)
        self.setupUic(self)


class Fot(QMainWindow, )


app = QApplication(sys.argv)
ex = Osnv()
ex.show()
sys.exit(app.exec_())