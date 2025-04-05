from anagrama import son_anagramas

def test_son_anagramas1():
    resultado = son_anagramas("roma","amor")
    assert resultado == True

def test_son_anagramas2():
    resultado = son_anagramas("hola","adios")
    assert resultado == False