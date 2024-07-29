import numpy as np

def fletcherReeves(f, x0, epsilon1, epsilon2, epsilon3, metodo):

    """
    Este método intenta encontrar un mínimo local de la función `f` utilizando gradiente conjugado con la actualización
    de Fletcher-Reeves.

    :param f: La función objetivo que se va a minimizar.
    :type f: function
    :param x0: El punto inicial desde donde comienza la optimización.
    :type x0: numpy.ndarray
    :param epsilon1: El umbral para la búsqueda de línea.
    :type epsilon1: float
    :param epsilon2: El umbral para el cambio relativo en `x`.
    :type epsilon2: float
    :param epsilon3: El umbral para la norma del gradiente bajo el cual se considera que la solución ha convergido.
    :type epsilon3: float
    :param metodo: El método de búsqueda de línea a utilizar.
    :type metodo: function
    :return: El punto donde se encontró el mínimo local.
    :rtype: numpy.ndarray
    :raises ValueError: Si `x0` no es un numpy.ndarray.
    
    :Ejemplo:

    >>> import numpy as np
    >>> def f(x):
    >>>     return np.sum(x**2)
    >>> def fibonacci_search(f, e, a, b):
    >>>     L = b - a
    >>>     fib = [0, 1]
    >>>     while len(fib) <= e + 2:
    >>>         fib.append(fib[-1] + fib[-2])
    >>>     k = 2
    >>>     while k < e:
    >>>         Lk = (fib[e - k + 2] / fib[e + 2]) * L
    >>>         x1 = a + Lk
    >>>         x2 = b - Lk
    >>>         fx1 = f(x1)
    >>>         fx2 = f(x2)
    >>>         if fx1 < fx2:
    >>>             b = x2
    >>>         elif fx1 > fx2:
    >>>             a = x1
    >>>         elif fx1 == fx2:
    >>>             a = x1
    >>>             b = x2
    >>>         k += 1
    >>>     return (a + b) / 2
    >>> x0 = np.array([2.0, 3.0])
    >>> epsilon1 = 0.001
    >>> epsilon2 = 0.001
    >>> epsilon3 = 0.001
    >>> result = fletcherReeves(himmelblau, x0, epsilon1, epsilon2, epsilon3, fibonacci_search)
    >>> print(result)

    """

    def gradiente(f, x, deltaX=0.001):
        grad = []
        for i in range(len(x)):
            xp = x.copy()
            xn = x.copy()
            xp[i] = xp[i] + deltaX
            xn[i] = xn[i] - deltaX
            grad.append((f(xp) - f(xn)) / (2 * deltaX))
        return np.array(grad)

    x = x0
    grad = gradiente(f, x)
    s = -grad
    k = 0

    while True:
        alpha = metodo(lambda alpha: f(x + alpha * s), e=epsilon1, a=0.0, b=1.0)
        x_next = x + alpha * s
        grad_next = gradiente(f, x_next)

        if np.linalg.norm(x_next - x) / np.linalg.norm(x) <= epsilon2 or np.linalg.norm(grad_next) <= epsilon3:
            break

        beta = np.linalg.norm(grad_next) ** 2 / np.linalg.norm(grad) ** 2
        s = -grad_next + beta * s

        x = x_next
        grad = grad_next
        k += 1

    return x