from src.tablaAsignacion import *
class Dni:
    def __init__(self, cadena = ""):
        self.correctLetter = False
        self.correctNumber = False
        self.table = TablaAsignacion()
        self.dni = cadena
        self.LARGE = 9

        ##Getters and Setters

    def setDni(self, cadena):
        self.dni = cadena

    def getDni(self):
        return self.dni

    def setCorrectLetter(self, result):
        self.correctLetter = result

    def getCorrectLetter(self):
        return self.correctLetter

    def setCorrectNumber(self, result):
        self.correctNumber = result

    def getCorrectNumber(self):
        return self.correctNumber


    def checkLarge(self):
        return len(self.dni) == self.LARGE


    def checkLetter(self):
        return self.dni[-1].isalpha()

    def checkLetterUpper(self):
        return self.dni[-1].isupper()

    def checkNumber(self):
        return self.dni[0:self.LARGE-1].isdigit()

    def checkValid(self):
        return self.checkLarge() and self.checkLetter() and self.checkLetterUpper() and self.checkNumber()




if __name__ == '__main__':
    dni = Dni("12345677A")

    print(dni.checkValid())
