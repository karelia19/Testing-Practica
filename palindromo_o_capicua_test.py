from palindromo_o_capicua import es_palindromo_o_capicua

def test_es_palindromo_o_capicua():
    resultado = es_palindromo_o_capicua(12321)
    assert resultado == True

def test_es_palindromo_o_capicua2():
    resultado = es_palindromo_o_capicua(123)
    assert resultado == False

def test_es_palindromo_o_capicua3():
    resultado = es_palindromo_o_capicua("hola")
    assert resultado == False

def test_es_palindromo_o_capicua4():
    resultado = es_palindromo_o_capicua("holaloh")
    assert resultado == True