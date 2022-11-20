from imports import *

class mainWindow(QWidget):
    names = ["Bin", "Dec", "Hex"]
    darkmode = False
    
    def __init__(self):
        super().__init__()
        apply_stylesheet(self, color[1])


        self.tela = QVBoxLayout(self)
        self.main = QFrame(self)

        #//////// - - - CORPO - - - ////////
        self.corpo = QVBoxLayout(self.main)
        
        #//// - - - Setup Buttons - - - ////
        self.upBut = QComboBox()
        self.upBut.setMinimumWidth(100) 
        for i in self.names:
            self.upBut.addItem(i)
        self.upBut.setCurrentIndex(1)
        self.downBut = QComboBox()
        self.downBut.setMinimumWidth(100) 
        for i in self.names:
            self.downBut.addItem(i)
        self.converter = QPushButton("Converter")
        self.converter.animateClick()
            
        #//// - - - Setup LineEdit - - - ////
        self.upLine = QLineEdit()
        self.upLine.setMinimumWidth(180)
        self.upLine.setPlaceholderText("Insira um número inteiro")
        self.downLine = QLineEdit()
        self.downLine.setMinimumWidth(180)
        self.downLine.setReadOnly(True)
        self.downLine.setPlaceholderText("O resultado aparecerá aqui")
        
        #///// - - - Setup Layout - - - /////
            #linha 1
        self.upLayout = QHBoxLayout()
        self.upLayout.addWidget(self.upBut)
        self.upLayout.addWidget(self.upLine)
        self.upLayout.setSpacing(10)
        
            #linha 2
        self.downLayout = QHBoxLayout()
        self.downLayout.addWidget(self.downBut)
        self.downLayout.addWidget(self.downLine)
        self.downLayout.setSpacing(10)

        #Seletores
        self.area = QVBoxLayout()
        self.area.addLayout(self.upLayout)
        self.area.addLayout(self.downLayout)
        self.area.setSpacing(8)
        
        #Botao
        self.placeBut = QVBoxLayout()
        self.placeBut.addWidget(self.converter)
        self.placeBut.setSpacing(0)

        
        #Seletores + Botao
        self.corpo.addStretch()
        self.corpo.addLayout(self.area)
        self.corpo.addLayout(self.placeBut)
        self.corpo.setSpacing(90)
        self.corpo.setContentsMargins(50, 50, 50, 50)
        self.corpo.addStretch()
    
        self.main.show()

        self.tela.addWidget(self.main)
        self.setLayout(self.tela)
        
        
        self.menu = QMenuBar()
        self.settings = QMenu("Configurações")
        self.dark = QAction(f"Modo Escuro")
        self.dark.triggered.connect(self.switch)
        self.settings.addAction(self.dark)
        self.menu.addMenu(self.settings)
        self.tela.setMenuBar(self.menu)
        self.setWindowTitle("Conversor")
        self.show()
        self.converter.clicked.connect(lambda: self.converterNum(self.downBut.currentText(), self.upLine.text() if self.upLine.text() else "", self.upBut.currentText()))
        
    def switch(self):
        self.darkmode = not self.darkmode
        if self.darkmode:
            apply_stylesheet(self, color[0])
        else:
            apply_stylesheet(self, color[1])
       
    def converterNum(self, mode, i, input):
        if mode == "Bin":
            if input == "Dec":
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
                        return self.resultado(i, convertido, mode)
                    else:
                        return f'Binário: 0'
                elif i == "":
                    pass
                else:
                    return self.downLine.setText(f'{i} não é um número inteiro!')
            elif input == "Hex":
                if i.isdigit():
                    num = int(i)
                    ...
                    convertido = str()
                    if num != 0:
                        return self.resultado(i, convertido, mode)
                    else:
                        return f'Binário: 0'
                else:
                    return self.downLine.setText(f'{i} não é um número inteiro!')
        elif mode == "Hex":
            if i.isdigit():
                num = int(i)
                ...
                convertido = str()
                if num != 0:
                    return self.resultado(i, convertido, mode)
                else:
                    return f'Hexadecimal: 0'
            else:
                return self.downLine.setText(f'{i} não é um número inteiro!')
        elif mode == "Dec":
            if i.isdigit():
                num = int(i)
                ...
                convertido = 0
                if num != 0:
                    return self.resultado(i, convertido, mode)
                else:
                    return f'Decimal: 0'
            else:
                return self.downLine.setText(f'{i} não é um número inteiro!')
       
            
    def resultado(self, input, output, convesion: str):
        if convesion == "Bin":
            return self.downLine.setText(f"O binário de {input} é {output}")
        elif convesion == "Dec":
            return self.downLine.setText(f"O decimal de {input} é {output}")
        elif convesion == "Hex":
            return self.downLine.setText(f"O hexadecimal de {input} é {output}")