import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from mainw import MainWindow
from calc import Calc
from foto import Foto
from checkCard import Check_Card
from coinFlip import Coin_Flip
from PIL import Image
from random import choice


class Osnv(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super(Osnv, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calc)
        self.pushButton_2.clicked.connect(self.check)
        self.pushButton_4.clicked.connect(self.coin)
        self.pushButton_5.clicked.connect(self.foto)
        self.callcalc = Cal(self)
        self.callfoto = Fot(self)
        self.callcheck = Check(self)
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

    def initUi(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        a = self.lineEdit.text()
        с = self.lineEdit_2.text()
        orig = Image.open(a)
        pixels = orig.load()
        x, y = orig.size
        red = orig.copy()
        pixeldsr = red.load()
        s = 10
        for i in range(x):
            for j in range(y):
                if i < s:
                    rr, g, b = pixeldsr[i, j]
                    pixeldsr[i, j] = rr, 0, 0
                    r, g, b = pixels[i, j]
                    pixels[i, j] = 0, g, b
                else:
                    rr, g, b = pixeldsr[i, j]
                    pixeldsr[i, j] = rr, 0, 0
                    r1, g, b = pixeldsr[i - 10, j]
                    r, g, b = pixels[i, j]
                    pixels[i, j] = r1, g, b
        orig.save(с)


class Check(QMainWindow, Check_Card):
    def __init__(self, parent=None):
        super(Check, self).__init__(parent)
        self.setupUicc(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.check)

    def check(self):
        card_number = self.lineEdit.text().replace(' ', '')

        digits = [int(char) for char in card_number]
        digits = digits[-1::-1]  # Reverse the array

        # double alternate digits (step 1)
        doubled = [(digit * 2) if ((i + 1) % 2 == 0) else digit \
                   for (i, digit) in enumerate(digits)]
        # subtract 9 which >= 10 (step 2)
        summed = [num if num < 10 else num - 9 \
                  for num in doubled]
        # step 3
        if sum(summed) % 10 == 0:
            self.statusBar().showMessage('Okey')
        else:
            self.statusBar().showMessage('Bad')


class Coin(QMainWindow, Coin_Flip):
    def __init__(self, parent=None):
        super(Coin, self).__init__(parent)
        self.setupUicf(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.flip)

    def flip(self):
        coin = ['Орёл', 'Решка']
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" "
                           "font-size:24pt;\">{}</span>"
                           "</p></body></html>".format(choice(coin)))

app = QApplication(sys.argv)
ex = Osnv()
ex.show()
sys.exit(app.exec_())