#!/bin/python3

import os
import sys
from itertools import combinations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
# Complejidad Tiempo: O(k^2 * n) donde k = chars unicos (k <= 26) → efectivamente O(n)
# Complejidad Espacio: O(n) — se almacena la lista filtrada por cada par
#

def alternate(s):
    unique_chars = set(s)

    # Si hay menos de 2 caracteres distintos, no se puede formar string alternante
    if len(unique_chars) < 2:
        return 0

    max_len = 0

    # Probar todas las combinaciones posibles de 2 letras (estrategia Greedy)
    for c1, c2 in combinations(unique_chars, 2):
        # Filtrar el string dejando solo c1 y c2
        filtered = [c for c in s if c == c1 or c == c2]

        # Verificar si los caracteres alternan (no hay dos iguales consecutivos)
        is_valid = all(filtered[i] != filtered[i+1] for i in range(len(filtered) - 1))

        if is_valid:
            max_len = max(max_len, len(filtered))

    return max_len


if __name__ == '__main__':
    # Modo HackerRank: escribe resultado en OUTPUT_PATH
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        l = int(input().strip())
        s = input()
        result = alternate(s)
        fptr.write(str(result) + '\n')
        fptr.close()
    else:
        # Modo local: lee de stdin e imprime en consola
        l = int(input("Longitud del string: "))
        s = input("Ingresa el string: ")
        print(f"Longitud maxima alternante: {alternate(s)}")
