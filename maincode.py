import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainw import MainWindow
from calc import Calc
from foto import Foto
from checkCard import Check_Card
from binbit import Bin_Dec
from coinFlip import Coin_Flip


class Osnv(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super(Osnv, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calc)
        self.pushButton_2.clicked.connect(self.check)
        self.pushButton_3.clicked.connect(self.bindec)
        self.pushButton_4.clicked.connect(self.coin)
        self.pushButton_5.clicked.connect(self.foto)
        self.callcalc = Cal(self)
        self.callfoto = Fot(self)
        self.callcheck = Check(self)
        self.callbin = BinDec(self)
        self.callcoin = Coin(self)

    def calc(self):
        self.callcalc.show()

    def foto(self):
        self.callfoto.show()

    def check(self):
        self.callcheck.show()

    def bindec(self):
        self.callbin.show()

    def coin(self):
        self.callcoin.show()


class Cal(QMainWindow, Calc):
    def __init__(self, parent=None):
        super(Cal, self).__init__(parent)
        self.setupUic(self)


class Fot(QMainWindow, Foto):
    def __init__(self, parent=None):
        super(Fot, self).__init__(parent)
        self.setupUif(self)


app = QApplication(sys.argv)
ex = Osnv()
ex.show()
sys.exit(app.exec_())