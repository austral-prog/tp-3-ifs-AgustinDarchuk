def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass

    contr = str(input())
    largo = len(contr)
    
    if largo < 8:
        print("Contraseña muy corta")
    if "0" in contr or "1" in contr or "2" in contr or "3" in contr or "4" in contr or "5" in contr or "6" in contr or "7" in contr or "8" in contr or "9" in contr:
        print("Contraseña valida")
    else:
        print("Debe contener un numero")
