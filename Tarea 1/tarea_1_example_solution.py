# Se define el primer método de la tarea. En este caso se llama
# separa_letras y tiene como entrada una variable llamada cadena.
def separa_letras(Cadena):
    # Se crean las variables que van a contener las salidas de la función
    Mayusculas = None
    Minusculas = None
    CodigoErrorExito = 0
    # Se verifica que la variable de entrada sea del tipo string
    if (isinstance(Cadena, str)):
        # Se verifica que la variable de entrada sean solo letras
        if (Cadena.isalpha()):
            # Se estipula que es un exito al
            # comprobarse los requerimientos de Cadena
            CodigoErrorExito = 0
            # Se separan los caracteres según si son mayusculas o minusculas
            Mayusculas = ""
            Minusculas = ""
            for element in Cadena:
                if (element.isupper()):
                    Mayusculas = Mayusculas + element
                else:
                    Minusculas = Minusculas + element
            # Se devuelven las variables de salida
            return (CodigoErrorExito, Mayusculas, Minusculas)
# Se asigna el codigo de error correspondiente y se hace return
        else:
            if (Cadena == ""):
                CodigoErrorExito = -300
            else:
                CodigoErrorExito = -200
            return (CodigoErrorExito, Mayusculas, Minusculas)
    else:
        CodigoErrorExito = -100
        return (CodigoErrorExito, Mayusculas, Minusculas)


# Se define el segundo método de la tarea, el cual tiene como entrada 2
# variables numéricas, una base y una potencia.
def potencia_manual(base, potencia):
    # Se declaran e inicializan en 0 las salidas del método, donde estado
    # es el código de error/éxito y result es el resultado de la potencia.
    estado = 0
    result = 0
    # Se verifica que los parámetros de entrada no sean de tipo string.
    if (isinstance(base, str) or isinstance(potencia, str)):
        estado = -400
        result = None
    else:
        # Se generan las respuestas esperadas para casos especiales.
        if (potencia == 0):
            result = 1
        elif (base == 0):
            result = 0
        else:
            # En caso de haber pasado todos los filtros, se procede a realizar
            # la potencia manual mediante sumas iterativas.
            # se inicializan las variables a utilizar en los ciclos for.
            res1 = 0
            result = base
            # La solución se basa en generar paquetes de sumatorias
            # de la cantidad de digitos que dictamine la base para
            # simular la multiplicacion.
            # result inicialmente es la base y conforme avanza
            # el ciclo for de la potencia, esta base se va actualizando
            # hasta alcanzar el resultado requerido.
            for i in range(potencia-1):
                for i in range(base):
                    res1 = res1 + result
                result = res1
                res1 = 0
    # Se devuelven estado y result como parámetros de salida.
    return (estado, result)