from imports import *
from conversoes.conver import defs

class mainWindow(QWidget):
    names = ["Bin", "Dec", "Hex"]
    darkmode = False
    a = color[0]
    
    def __init__(self):
        super().__init__()
        apply_stylesheet(self, self.a)


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
        self.converter.setShortcut('Enter')
        
        self.upLine.setFocus()
    
    # ///// - - - Dark Mode - - - /////    
    def switch(self):
        self.darkmode = not self.darkmode
        if self.a == color[0]:
            self.a = color[1]
        else:
            self.a = color[0]
        apply_stylesheet(self, self.a)
    
    #///// - - - Função para converter - - - /////   
    def converterNum(self, mode, i, input):
        
        if input == "Dec":
            if mode == "Bin":
                return retorno.fromDec(self, mode, i, 2)
            elif mode == "Hex":
                return retorno.fromDec(self, mode, i, 16)
            elif mode == "Dec":
                return self.downLine.setText(f'Bases iguais - {i}')
            
        elif input == "Bin":
            if mode == "Dec":
                return retorno.toDec(self, mode, i, 2)
            elif mode == "Bin":
                return self.downLine.setText(f'Bases iguais - {i}')
            elif mode == "Hex":
                dec = str(defs.inteiroFed(self, str(i), 2))
                return retorno.fromDec(self, mode, dec, 16)
            
        elif input == "Hex":
            if mode == "Dec":
                return retorno.toDec(self, mode, i, 16)
            elif mode == "Bin":
                dec = str(defs.inteiroFed(self, str(i), 16))
                return retorno.fromDec(self, mode, dec, 2)
            elif input == "Hex":
                return self.downLine.setText(f'Bases iguais - {i}') 
            
    def resultado(self, input, output, convesion: str):
        entrada = input.replace('.', ',')
        if convesion == "Bin":
            return self.downLine.setText(f"O binário de {entrada} é {output}")
        elif convesion == "Dec":
            return self.downLine.setText(f"O decimal de {entrada} é {output}")
        elif convesion == "Hex":
            return self.downLine.setText(f"O hexadecimal de {entrada} é {output}")