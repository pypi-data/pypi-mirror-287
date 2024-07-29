
def fibonacci_search(f, e, a, b):
    
    """
    Encuentra el mínimo de una función unidimensional utilizando el método de búsqueda de Fibonacci.

    La búsqueda de Fibonacci es un método de optimización unidimensional que utiliza la serie de Fibonacci para reducir el intervalo de búsqueda de manera eficiente.

    :param f: La función objetivo que se desea minimizar.
    :type f: function
    :param e: El número deseado de evaluaciones.
    :type e: int
    :param a: El límite inferior del intervalo de búsqueda.
    :type a: float
    :param b: El límite superior del intervalo de búsqueda.
    :type b: float
    :return: El punto en el intervalo \([a, b]\) donde la función tiene su mínimo.
    :rtype: float

    :Ejemplo:

    >>> def funcion_objetivo(x):
    >>>     return (x - 2)**2
    >>> minimo = fibonacci_search(funcion_objetivo, 10, 0, 4)
    >>> print(f"Resultado: x = {minimo}, f(x) = {funcion_objetivo(minimo)}")

    """
    
    L = b - a

    fib = [0, 1]
    while len(fib) <= e +2:
        fib.append(fib[-1] + fib[-2])

    
    k = 2

    while k < e:
        Lk = (fib[e - k + 2] / fib[e+ 2]) * L

        x1 = a + Lk
        x2 = b - Lk

        fx1 = f(x1)
        fx2 = f(x2)

        if fx1 < fx2:
            b = x2
        elif fx1 > fx2:
            a = x1
        elif fx1 == fx2:
            a=x1
            b=x2

        
        k += 1

    return a+b/2