def producto_escalar(escalar,vector):
    """
    num, list of num -> list of num

    "Funcion que calcula el producto escalar de un vector"

    >>> producto_escalar(2, (1,2,3))
    [2, 4, 6]

    :param escalar: El producto escalar
    :param vector: El vector ingresado
    :return: El producto escalar del vector
    """

    res = []
    cont = 0
    while cont < len(vector):
        res.append(escalar * vector[cont])
        cont += 1
    return res