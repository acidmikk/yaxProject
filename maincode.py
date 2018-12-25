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
        self.a = 0
        self.b = 0
        self.op = ['']
        self.pushButton_4.clicked.connect(self.svap_stack)
        self.pushButton_9.clicked.connect(self.svap_stack)
        self.pushButton_10.clicked.connect(self.svap_stack)
        self.pushButton_14.clicked.connect(self.svap_stack)
        self.pushButton_18.clicked.connect(self.svap_stack)
        self.pushButton_19.clicked.connect(self.svap_stack)
        self.pushButton_20.clicked.connect(self.svap_stack)
        self.pushButton.clicked.connect(self.nam_lcd)
        self.pushButton_2.clicked.connect(self.nam_lcd)
        self.pushButton_3.clicked.connect(self.nam_lcd)
        self.pushButton_6.clicked.connect(self.nam_lcd)
        self.pushButton_7.clicked.connect(self.nam_lcd)
        self.pushButton_8.clicked.connect(self.nam_lcd)
        self.pushButton_11.clicked.connect(self.nam_lcd)
        self.pushButton_12.clicked.connect(self.nam_lcd)
        self.pushButton_13.clicked.connect(self.nam_lcd)
        self.pushButton_16.clicked.connect(self.nam_lcd)
        self.pushButton_5.clicked.connect(self.clear)

    def clear(self):
        self.b = 0
        self.lcdNumber.display(self.b)

    def nam_lcd(self):
        c = self.sender().text()
        self.b = self.b*10 + int(c)
        self.lcdNumber.display(self.b)

    def svap_stack(self):
        if len(self.op) == 1:
            self.op.append(self.sender().text())
            self.a = self.b
            self.b = 0
            self.lcdNumber.display(self.a)
        else:
            self.op[0] = self.op[1]
            self.op[1] = self.sender().text()
            op = self.op[0]
            if op == 'x^y':
                self.a = self.a ** self.b
                self.lcdNumber.display(self.a)
            if op == '/':
                self.a = self.a / self.b
                self.lcdNumber.display(self.a)
            if op == '√':
                self.a = self.a ** (1 / self.b)
                self.lcdNumber.display(self.a)
            if op == '*':
                self.a = self.a * self.b
                self.lcdNumber.display(self.a)
            if op == '+':
                self.a = self.a + self.b
                self.lcdNumber.display(self.a)
            if op == '-':
                self.a = self.a - self.b
                self.lcdNumber.display(self.a)


class Fot(QMainWindow, Foto):
    def __init__(self, parent=None):
        super(Fot, self).__init__(parent)
        self.setupUif(self)
        self.initUi()

    #def initUi(self):



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