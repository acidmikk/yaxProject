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
        self.initUi()

    def initUi(self):
        a = 0
        b = 0
        op = ''
        lcd = a
        if self.pushButton_4.clicked.connect() or \
                self.pushButton_9.clicked.connect() or \
                self.pushButton_10.clicked.connect() or \
                self.pushButton_14.clicked.connect() or \
                self.pushButton_18.clicked.connect() or \
                self.pushButton_19.clicked.connect():
            lcd = b
            if self.pushButton_4.clicked.connect():
                op = 'step'
            if self.pushButton_9.clicked.connect():
                op = '/'
            if self.pushButton_10.clicked.connect():
                op = 'kor'
            if self.pushButton_14.clicked.connect():
                op = '*'
            if self.pushButton_18.clicked.connect():
                op = '+'
            if self.pushButton_19.clicked.connect():
                op = '-'
        if self.pushButton_20.clicked.connect():
            if op == 'step':
                self.lcdNumber.display(a ** b)
            if op == '/':
                self.lcdNumber.display(a / b)
            if op == 'kor':
                self.lcdNumber.display(a // (1 / b))
            if op == '*':
                self.lcdNumber.display(a * b)
            if op == '+':
                self.lcdNumber.display(a + b)
            if op == '-':
                self.lcdNumber.display(a - b)
        if self.pushButton.clicked.connect():
            lcd = lcd * 10 + 1
        if self.pushButton_2.clicked.connect():
            lcd = lcd * 10 + 2
        if self.pushButton_3.clicked.connect():
            lcd = lcd * 10 + 3
        if self.pushButton_6.clicked.connect():
            lcd = lcd * 10 + 4



class Fot(QMainWindow, Foto):
    def __init__(self, parent=None):
        super(Fot, self).__init__(parent)
        self.setupUif(self)


class Check(QMainWindow, Check_Card):
    def __init__(self, parent=None):
        super(Check, self).__init__(parent)
        self.setupUicc(self)


class BinDec(QMainWindow,Bin_Dec):
    def __init__(self, parent=None):
        super(BinDec, self).__init__(parent)
        self.setupUib(self)


class Coin(QMainWindow, Coin_Flip):
    def __init__(self, parent=None):
        super(Coin, self).__init__(parent)
        self.setupUicf(self)


app = QApplication(sys.argv)
ex = Osnv()
ex.show()
sys.exit(app.exec_())