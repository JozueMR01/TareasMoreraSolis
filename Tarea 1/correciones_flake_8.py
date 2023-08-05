# Este pequeño código contiene tres errores que son detectados por flake8
# a continuación se mencionan cuales son.

# Corrección 1: se comenta la librería en desuso para
# no importarla innecesariamente:
# import pytest

def errores():
    # Corrección 2: se añaden espacios antes y después del signo "=":
    error = "Este código tiene 3 errores de formato"
    # Correción 3: se deja espacio después de la palabra clave "return":
    return (error)
