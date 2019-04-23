def producto_punto(vector_1, vector_2):
    """
    (list of num, list of num) -> num
    Calcula el producto punto de dos vectores
    >>> producto_punto([1, 2, 3], [1, 2, 3])
    14
    >>> producto_punto([2, 2, 2], [1, 2, 3])
    12
    >>> producto_punto([1, 2, 3, 4], [1, 2, 3])
    Traceback (most recent call last):
    ...
    ValueError: Los vectores tienen diferente dimensión

    :param v1:
    :param v2:
    :return:
    """
    if len(vector_1) == len(vector_2):
       resultado = 0
       for i in range(0, len(vector_1)):
           resultado += vector_1[i] * vector_2[i]
       return resultado
    else:
       raise ValueError('Los vectores tienen diferente dimensión')