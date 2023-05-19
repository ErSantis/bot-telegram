def grado_recurrencia(relacion):
    # Separamos los términos de la relación
    terminos = relacion.split()

    # Encontramos la longitud de la relación
    n = len(terminos)

    # Encontramos los coeficientes de la relación
    coeficientes = []
    for i in range(n):
        if terminos[i] == '+':
            continue
        elif terminos[i] == '-':
            coeficientes.append(-1 * int(terminos[i+1]))
        else:
            coeficientes.append(int(terminos[i]))

    # Encontramos el grado de la relación
    grado = 0
    for i in range(n):
        if terminos[i].startswith('f(n-'):
            indice = int(terminos[i][4])
            if indice > grado:
                grado = indice

    # Retornamos el grado de la relación
    return grado

grado_recurrencia('4f(n-1) - 4f(n-2) + n')