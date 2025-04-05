def son_anagramas(palabra1: str, palabra2: str) -> bool:
    
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    
    return sorted(palabra1) == sorted(palabra2)

