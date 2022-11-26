from conversoes.conver import defs

class retorno:
    def fromDec(self, mode, a, base):
        if a == "":
            return self.downLine.setText('')
        i = a.replace(',', '.')
        if i.find('.') == -1:
            inteiro = defs.inteiroDef(self, i, base)
            if inteiro != None:
                return self.resultado(i, inteiro, mode)
            else:
                self.downLine.setText(f'{i} não é um número válido')
        elif i.find('.') >= 0:
            numeroSplit = []
            numeroSplit = i.split('.')
            inteiro = defs.inteiroDef(self, numeroSplit[0], base)
            decimal = str(defs.decimalDef(self, numeroSplit[1], base))
            if inteiro == None or decimal == None:
                return self.downLine.setText(f'{a} não é um número válido.')
            convertido = f'{inteiro},{decimal[:5]}'
            return self.resultado(i, convertido, mode)
        
    def toDec(self, mode, a, base):
        if a == "":
            return self.downLine.setText('')
        i = a.replace(',', '.')
        if i.find('.') == -1:
            inteiro = defs.inteiroFed(self, i, base)
            if inteiro != None:
                return self.resultado(i, inteiro, mode)
            else:
                self.downLine.setText(f'{i} não é um número válido.')
        elif i.find('.') >= 0:
            self.downLine.setText(f'Desculpe, não foi possível converter.')