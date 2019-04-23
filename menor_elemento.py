def menor_elemento(vector):
    '''
    Funcion que define cual es el mayor elemento del vector

    list of num -> num

    >>> menor_elemento([1,2,3])
    1
    >>> menor_elemento([4,5,6])
    4

    :param vector: Vector a calcular el mayor elemento
    :return: El elemento mayor del vector
    '''

    menor = min(vector)

    for i in range(len(vector)):
        return menor
