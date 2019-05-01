def s_vectores(vector_1,vector_2):
    '''
    Calcula la suma de dos vectores

    (list of num, list of num) -> list of num2

    >>> s_vectores([1,2,3], [3,2,1])
    [4, 4, 4]
    >>> s_vectores([5,5,5], [5,5,5])
    [10, 10, 10]
    >>> s_vectores([1,2,3,4], [5,6,7])
    Traceback (most recent call last):
    ...
    ValueError: Los vectores tienen diferente dimesión

    :param vector_1: El vector ingresado
    :param vector_2: El vector a sumar
    :return: La suma de los vectores
    '''

    if len(vector_1) == len(vector_2):
        resultante = []
        for i in range(0, len(vector_1)):
            resultante.append(vector_1[i] + vector_2[i])
        return resultante
    else:
        raise ValueError('Los vectores tienen diferente dimesión')

