#!/bin/python3

import os
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# Complejidad Tiempo: O(n) — se recorre el string una sola vez
# Complejidad Espacio: O(1) — solo se usa un contador entero
#

def camelcase(s):
    # Cada letra mayuscula = inicio de nueva palabra
    # Se suma 1 por la primera palabra (siempre minuscula)
    return sum(1 for c in s if c.isupper()) + 1


if __name__ == '__main__':
    # Modo HackerRank: escribe resultado en OUTPUT_PATH
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        s = input()
        result = camelcase(s)
        fptr.write(str(result) + '\n')
        fptr.close()
    else:
        # Modo local: lee de stdin e imprime en consola
        s = input("Ingresa el string CamelCase: ")
        print(f"Numero de palabras: {camelcase(s)}")
