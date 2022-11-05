import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
import qdarktheme

modo = 0

def calcular(i):
    match modo:
        case 0:
            if i.isdigit():
                num = int(i)
                bin = list()
                while num >= 2:
                    bin.append(num % 2)
                    num = num // 2
                bin.append(1)
                bin.reverse()
                convertido = str()
                for j in bin:
                    convertido = convertido + str(j)
                if num != 0:
                    return f'Binário: {convertido}'
                else:
                    return f'Binário: 0'
            else:
                return f'Insira um número inteiro!'
        case 1:
            print(widget.geometry())
            return f'Lógica ainda não foi implementada a este modo!'
        case 2:
            return f'Lógica ainda não foi implementada a este modo!'

def mudarTexto(i, j: QLabel):
    j.setText(calcular(i))

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


        self.layout = QVBoxLayout(self)

        self.label = QLabel('O resultado aparecerá aqui!')
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setContentsMargins(80, 40, 80, 60)
        self.texto = QLineEdit()
        self.texto.setAlignment(Qt.AlignHCenter)
        self.texto.setContentsMargins(80, 100, 80, 0)
        self.layoutH = QHBoxLayout()
        self.layoutV = QVBoxLayout()
        self.layoutV.addWidget(self.texto)
        self.layoutV.addWidget(self.label)
        self.buttonBin = QPushButton('Binário')
        self.buttonHex = QPushButton('Hexadecimal')
        self.buttonDec = QPushButton('Decimal')
        self.button = QPushButton('Converter')
        self.button.setShortcut(QKeySequence(Qt.Key_Enter) or QKeySequence(Qt.Key_Return))

        #func dos botoes
        self.buttonBin.clicked.connect(lambda: self.setMode(0))
        self.buttonDec.clicked.connect(lambda: self.setMode(1))
        self.buttonHex.clicked.connect(lambda: self.setMode(2))
        self.button.clicked.connect(lambda: mudarTexto(self.texto.text(), self.label))
        
        #layout de botões
        self.layoutH.addWidget(self.buttonBin)
        self.layoutH.addWidget(self.buttonDec)
        self.layoutH.addWidget(self.buttonHex)

        #layout da tela
        self.layout.addLayout(self.layoutH)
        self.layout.addLayout(self.layoutV)
        self.layout.addWidget(self.button)

    def setMode(self, x):
        global modo
        modo = x
        self.label.setText('O resultado aparecerá aqui!')
        self.texto.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.setWindowTitle('Conversor de bases')
    widget.setGeometry(0, 0, 502, 338)
    widget.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
