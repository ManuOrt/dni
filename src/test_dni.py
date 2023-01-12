from src.dni import Dni


def test_dni_constructor():
    dni = Dni("41573239A")
    assert dni.getDni() == "41573239A"


def test_dni_large():
    dni = Dni("41573239A")
    assert dni.checkLarge() == True
    dni2 = Dni("41573239AA")
    assert dni2.checkLarge() == False


def test_dni_letter():
    dni = Dni("41573239A")
    assert dni.checkLetter() == True
    dni2 = Dni("415732393")
    assert dni2.checkLetterUpper() == False


def test_dni_upper():
    dni = Dni("41573239A")
    assert dni.checkLetterUpper() == True
    dni2 = Dni("41573239a")
    assert dni2.checkLetterUpper() == False


def test_dni_number():
    dni = Dni("41573239A")
    assert dni.checkNumber() == True
    dni2 = Dni("415732392a")
    assert dni2.checkLetterUpper() == False


def test_dni_valid():
    dni = Dni("41573239A")
    assert dni.checkValid() == True
    dni2 = Dni("41573239aa")
    assert dni2.checkLetterUpper() == False

