import numpy as np

def busquedaDorada(funcion, e:float, a:float=None, b:float=None)->float:
    
    """
    Encuentra el mínimo de una función utilizando el método de búsqueda dorada.

    La búsqueda dorada es un método de optimización unidimensional basado en la proporción áurea para reducir el intervalo de búsqueda de manera eficiente.

    :param funcion: La función objetivo.
    :type funcion: function
    :param e: La tolerancia para el criterio de convergencia del método.
    :type e: float
    :param a: El límite inferior del intervalo de búsqueda. Si no se proporciona, se debe especificar.
    :type a: float, opcional
    :param b: El límite superior del intervalo de búsqueda. Si no se proporciona, se debe especificar.
    :type b: float, opcional
    :return: El punto en el intervalo \([a, b]\) donde la función tiene su mínimo.
    :rtype: float

    :Ejemplo:

    >>> import numpy as np
    >>> def funcion_objetivo(x):
    >>>     return (x - 2)**2
    >>> minimo = busquedaDorada(funcion_objetivo, 1e-5, 0, 4)
    >>> print(f"Resultado: x = {minimo}, f(x) = {funcion_objetivo(minimo)}")
    >>> 
    """
    
    def regla_eliminacion(x1, x2, fx1, fx2, a, b)->tuple[float, float]:
        if fx1>fx2:
            return x1, b
        
        if fx1<fx2:
            return a, x2
        
        return x1, x2 

    def w_to_x(w:float, a, b)->float:
        return w*(b-a)+a 
    
    phi=(1 + np.math.sqrt(5) )/ 2 - 1
    aw, bw=0,1
    Lw=1
    k=1

    while Lw>e:
        w2=aw+phi*Lw
        w1=bw-phi*Lw
        aw, bw=regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)), funcion(w_to_x(w2, a, b)), aw, bw)
        k+=1
        Lw=bw-aw

    return(w_to_x(aw, a, b)+w_to_x(bw, a, b))/2
