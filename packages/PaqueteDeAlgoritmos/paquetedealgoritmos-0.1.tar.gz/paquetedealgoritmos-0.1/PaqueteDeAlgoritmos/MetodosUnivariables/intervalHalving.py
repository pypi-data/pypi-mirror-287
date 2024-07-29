
def interval_halving_method(f, e, a, b):
    
    """
    Encuentra el mínimo de una función unidimensional utilizando el método de reducción del intervalo.

    El método de reducción del intervalo, o **Interval Halving**, busca minimizar una función unidimensional reduciendo el intervalo de búsqueda en cada iteración, eligiendo entre dos puntos que se encuentran a la mitad de la longitud del intervalo.

    :param f: La función objetivo.
    :type f: function
    :param e: La tolerancia para la longitud del intervalo de búsqueda, el proceso se detiene cuando \(|b - a| < e\).
    :type e: float
    :param a: El límite inferior del intervalo de búsqueda.
    :type a: float
    :param b: El límite superior del intervalo de búsqueda.
    :type b: float
    :return: El punto en el intervalo \([a, b]\) donde la función tiene su mínimo.
    :rtype: float

    :Ejemplo:

    >>> def funcion_objetivo(x):
    >>>     return (x - 2)**2
    >>> minimo = interval_halving_method(funcion_objetivo, 1e-5, 0, 4)
    >>> print(f"Resultado: x = {minimo}, f(x) = {funcion_objetivo(minimo)}")
    """
    L = b - a
    xm = (a + b) / 2

    while True:
        x1 = a + (L / 4)
        x2 = b - (L / 4)

        fx1 = f(x1)
        fx2 = f(x2)
        fxm = f(xm)

        if fx1 < fxm:
            b = xm
            xm = x1
        else:
            if fx2 < fxm:
                a = xm
                xm = x2
            else:
                a = x1
                b = x2

        L = b - a
        if abs(L) < e:
            return x1+x2/2 
        