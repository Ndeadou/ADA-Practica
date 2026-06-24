# Practica-ADA — Examen Practico (50%)

Repositorio del examen práctico de Algoritmos y Estructuras de Datos.  
Contiene 2 ejercicios seleccionados de [HackerRank](https://www.hackerrank.com/), con solución en Python y análisis de complejidad computacional.

---

## Ejercicios

| # | Problema | Categoría | Complejidad Tiempo | Complejidad Espacio |
|---|----------|-----------|-------------------|---------------------|
| 1 | [CamelCase](#ejercicio-1--camelcase) | Strings | O(n) | O(1) |
| 2 | [Alternating Characters](#ejercicio-2--alternating-characters) | Greedy | O(n) | O(n) |

---

## Ejercicio 1 — CamelCase

**Problema:** Dada una cadena en formato CamelCase, contar cuántas palabras contiene.

**Ejemplo:**
```
Input:  saveChangesInTheEditor
Output: 5
```

**Solución:** Se cuentan las letras mayúsculas (cada una representa el inicio de una nueva palabra) y se suma 1 por la primera palabra.

```python
def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1
```

**Complejidad:**
- ⏱ Tiempo: `O(n)` — se recorre el string una sola vez
- 💾 Espacio: `O(1)` — solo se usa un contador entero

---

## Ejercicio 2 — Alternating Characters

**Problema:** Dada una cadena, eliminar caracteres (todas las instancias a la vez) hasta que queden solo dos letras que alteren entre sí. Retornar la longitud máxima posible.

**Ejemplo:**
```
Input:  beabeefeab
Output: 5  (→ "babab", eliminando e y f)
```

**Solución (Greedy):** Se prueban todas las combinaciones posibles de 2 letras, se filtra el string y se verifica si alternan correctamente. Se retorna la mayor longitud válida.

```python
from itertools import combinations

def alternate(s):
    unique_chars = set(s)
    if len(unique_chars) < 2:
        return 0
    max_len = 0
    for c1, c2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c == c1 or c == c2]
        is_valid = all(filtered[i] != filtered[i+1] for i in range(len(filtered) - 1))
        if is_valid:
            max_len = max(max_len, len(filtered))
    return max_len
```

**Complejidad:**
- ⏱ Tiempo: `O(k² * n)` donde k = caracteres únicos (k ≤ 26, constante) → efectivamente `O(n)`
- 💾 Espacio: `O(n)` — se almacena la lista filtrada

---

## Cómo ejecutar los programas

### Requisitos
- Python 3.x instalado ([descargar aquí](https://www.python.org/downloads/))
- No requiere librerías externas

### Opción 1 — Ejecutar directamente con input manual

```bash
# Ejercicio 1
python ejercicio1_camelcase/solution.py
# Escribe el string CamelCase y presiona Enter
# Ejemplo: saveChangesInTheEditor

# Ejercicio 2
python ejercicio2_alternating/solution.py
# Escribe la longitud y luego el string
# Ejemplo:
# 10
# beabeefeab
```

### Opción 2 — Ejecutar con archivo de entrada

```bash
# Crear archivo con el input
echo "saveChangesInTheEditor" > input.txt

# Ejecutar redirigiendo el input
python ejercicio1_camelcase/solution.py < input.txt
```

### Opción 3 — Ejecutar en HackerRank
Copiar el contenido de `solution.py` directamente en el editor de HackerRank.

---

## Estructura del repositorio

```
Practica-ADA/
├── README.md
├── ejercicio1_camelcase/
│   └── solution.py
└── ejercicio2_alternating/
    └── solution.py
```

---

## Autor
**Ndeadou** — Examen Práctico ADA, junio 2026
