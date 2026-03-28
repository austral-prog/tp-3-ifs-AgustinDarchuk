def positive():
    """
    Ejercicio 1 - Clasificar Número

    Leer un número entero mediante input(). Determinar si es positivo, negativo o cero
    e imprimir el resultado correspondiente.

    Ejemplo:
        Para la entrada "5", la salida esperada es:
        El numero es positivo

        Para la entrada "-3", la salida esperada es:
        El numero es negativo

        Para la entrada "0", la salida esperada es:
        El numero es cero
    """
    pass

    numero = int(input())
    
    if numero > 0:
        print(f'El numero es positivo')
    if numero < 0:
        print(f'El numero es negativo')
    if numero == 0:
        print(f'El numero es cero')
