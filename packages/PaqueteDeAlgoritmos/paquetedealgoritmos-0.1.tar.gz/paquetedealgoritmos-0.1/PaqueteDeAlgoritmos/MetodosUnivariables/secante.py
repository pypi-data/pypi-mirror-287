import numpy as np

def secante(f, e, a, b):
    """
    Encuentra una raíz de una función unidimensional utilizando el método de la secante.

    El método de la secante es una técnica iterativa para encontrar soluciones de ecuaciones no lineales. A diferencia del método de Newton-Raphson, la secante no requiere el cálculo de la derivada, sino que utiliza una aproximación basada en dos puntos previos.

    :param f: La función para la cual se busca una raíz.
    :type f: function
    :param e: La tolerancia para el criterio de convergencia.
    :type e: float
    :param a: El límite inferior del intervalo de búsqueda.
    :type a: float
    :param b: El límite superior del intervalo de búsqueda.
    :type b: float
    :return: El valor de \(x\) que aproxima una raíz de la función.
    :rtype: float

    :Ejemplo:

    >>> def funcion_objetivo(x):
    >>>     return x**3 - x - 2
    >>> raiz = secante(funcion_objetivo, 1e-5, 1.0, 2.0)
    >>> print(f"Raíz encontrada: x = {raiz}, f(x) = {funcion_objetivo(raiz)}")

    """
    
    def primera_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - f(x - delta)) / (2 * delta)
       
    a = np.random.uniform(a, b)
    b = np.random.uniform(a, b)
    x1 = a
    x2 = b
    
    while True:
        z= x2- ( (primera_derivada(x2, f))  / (    ( (primera_derivada(x2, f)) - (primera_derivada(x1,f)) ) /   (x2-x1)   )     )
        f_primaz = primera_derivada(z, f)
    
        if abs(x2 - x1) < e: 
            break
        elif f_primaz < 0:
            x1 = z
        elif f_primaz > 0:
            x2 = z

    return x1+x2/2