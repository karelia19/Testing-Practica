def es_palindromo_o_capicua(texto: int | str):
    if type(texto) == int:
        texto = str(texto)  
        return texto == texto[::-1]
    
    else:
        texto_limpio = texto.replace(" ", "").lower()  
        return texto_limpio == texto_limpio[::-1]
