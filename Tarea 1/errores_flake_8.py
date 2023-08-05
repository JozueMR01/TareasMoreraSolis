# Este pequeño código contiene tres errores que son detectados por flake8
# a ontinuación se mencionan cuales son.

# Error 1: se importa una librería que no se usa
import pytest


def errores():
    # Error 2: no se deja espacios antes y después del signo =
    error="Este código tiene 3 errores de formato"
    # Error 3: no se deja espacio después de la palabra clave "return"
    return(error)
