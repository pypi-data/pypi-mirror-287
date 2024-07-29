import numpy as np

def biseccion(f, e, a, b):
    """
    Realiza la búsqueda de la raíz de la derivada de la función `f` utilizando el método de bisección.

    Este método encuentra un punto donde la primera derivada de la función `f` es cero, lo cual puede indicar un máximo o un mínimo local.

    :param f: La función objetivo
    :type f: function
    :param e: La tolerancia para el criterio de convergencia.
    :type e: float
    :param a: El límite inferior del intervalo de búsqueda.
    :type a: float
    :param b: El límite superior del intervalo de búsqueda.
    :type b: float
    :return: El punto donde la primera derivada de `f` es cero.
    :rtype: float

    :Ejemplo:

    >>> import numpy as np
    >>> def funcion_objetivo(x):
    >>>     return (x - 2)**2
    >>> resultado = biseccion(funcion_objetivo, 1e-5, 0, 4)
    >>> print(resultado)
    """
    
    def primera_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - f(x - delta)) / (2 * delta)
    
    a = np.random.uniform(a, b)
    b = np.random.uniform(a, b)
    
    while(primera_derivada(a,f) > 0):
        a = np.random.uniform(a, b)
    
    while (primera_derivada(b,f) < 0): 
        b = np.random.uniform(a, b)
    
    x1=a
    x2=b
    
    while True:
        z = (x1 + x2) / 2
        f_primaz = primera_derivada(z, f)
    
        if abs(f_primaz) < e:  
            break
        elif f_primaz < 0:
            x1 = z
        elif f_primaz > 0:
            x2 = z

    return x1+x2/2
