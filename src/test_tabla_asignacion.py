from src.dni import TablaAsignacion

def test_tabla_get_letter():
    table = TablaAsignacion()
    assert table.getLetter(3) == "A"
    assert table.getLetter(30) is False


def test_tabla_check_letter():
    table = TablaAsignacion()
    assert table.checkLetter("A")
    assert table.checkLetter("I") is False


def test_tabla_module():
    table = TablaAsignacion()
    assert table.getModule() == 23


def test_tabla_calcular():
    table = TablaAsignacion()
    dni = ["78484464", "72376173", "01817200", "95882054", "63587725", "26861694", "21616083", "26868974",
           "40135330", "89044648", "34168723", "76857238", "66714505", "66499420"]

    solucion = ["T", "A", "Q", "E", "Q", "V", "Q", "Y", "P", "X", "S", "R", "S", "A"]
    index = 0
    for dnis in dni:
        assert table.calcularLetra(dnis) == solucion[index]
        index += 1


