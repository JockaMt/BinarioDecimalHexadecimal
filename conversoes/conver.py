class defs:
    letras = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    letras1 = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    def inteiroDef(self, i, base):
        try:
            num = int(i)
            bin = list()
            while num >= base:
                bin.append(num % base)
                num = num // base
            bin.append(num)
            bin.reverse()
            convertido = str()
            for j in bin:
                if j > 9:
                    j = defs.letras[j]
                convertido = convertido + str(j)
            if num != 0:
                return convertido
            else:
                return 0
        except:
            return
        
    def decimalDef(self, i, base):
        try:
            num = float('.' + str(i))
            bin = list()
            aux = 0
            while num != 0:
                num *= base
                if num == aux:
                    break
                aux = num
                bin.append(int(num))
                num = num - int(num)
            convertido = str()
            for j in bin:
                if j > 9:
                    j = defs.letras[j]
                convertido = convertido + str(j)
            return convertido
        except:
            return
    
    def inteiroFed(self, entrada, base):
        try:
            lista = list()
            for i in entrada:
                if i.isdigit():
                    lista.append(int(i))
                else:
                    lista.append(i)
            for item in lista:
                if item in defs.letras1:
                    lista[lista.index(item)] = defs.letras1[item]
            lista.reverse()
            res = list()
            for index, num in enumerate(lista):
                res.append(num * (base ** index))
            return sum(res)
        except:
            print(' - Error - ')

