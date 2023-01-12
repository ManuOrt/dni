
class TablaAsignacion:

    def __init__(self):
        self.table = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J',
                      'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    def getLetter(self, posicion):
        try:
            return self.table[posicion]
        except:
            return False

    def checkLetter(self, letter):
        try:
            return letter in self.table
        except:
            return False


    def getModule(self):
        return len(self.table)


    def calcularLetra(self, DNI):
        posicion = int(DNI) % self.getModule()
        return self.getLetter(posicion)

    def showTabla(self):
        print(self.table)



if __name__ == '__main__':
    tabla = TablaAsignacion()

    print(tabla.calcularLetra("43182623"))
