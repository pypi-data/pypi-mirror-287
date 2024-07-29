import numpy as np

def newton(f, x0, epsilon1, epsilon2, maxiter, metodo):

    """
    Este método intenta encontrar un mínimo local de la función `f` utilizando el método de Newton, que emplea tanto el gradiente como la matriz Hessiana de la función objetivo.

    :param f: La función objetivo.
    :type f: function
    :param x0: Punto inicial.
    :type x0: list or numpy.ndarray
    :param epsilon1: Criterio de convergencia basado en el gradiente.
    :type epsilon1: float
    :param epsilon2: Criterio de convergencia basado en el cambio en las variables.
    :type epsilon2: float
    :param maxiter: Número máximo de iteraciones permitidas.
    :type maxiter: int
    :param metodo: Método de búsqueda de línea para determinar el paso óptimo.
    :type metodo: function
    :return: El punto donde se encontró el mínimo local.
    :rtype: numpy.ndarray
    
    :Ejemplo:

    >>> import numpy as np
    >>> def rosenbrock(x):
    >>>     return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
    >>> def fibonacci_search(f, e, a, b):
    >>>     L = b - a
    >>>     fib = [0, 1]
    >>>     while len(fib) <= e +2:
    >>>         fib.append(fib[-1] + fib[-2])
    >>>     k = 2
    >>>     while k < e:
    >>>         Lk = (fib[e - k + 2] / fib[e+ 2]) * L
    >>>         x1 = a + Lk
    >>>         x2 = b - Lk
    >>>         fx1 = f(x1)
    >>>         fx2 = f(x2)
    >>>         if fx1 < fx2:
    >>>             b = x2
    >>>         elif fx1 > fx2:
    >>>             a = x1
    >>>         elif fx1 == fx2:
    >>>             a=x1
    >>>             b=x2
    >>>         k += 1
    >>>     return (a+b)/2
    >>> x0=np.array([0.0, 0.0])
    >>> epsilon1=0.001
    >>> epsilon2=0.001
    >>> max_iter=100
    >>> result = newton(himmelblau, x0, epsilon1, epsilon2, 1000, fibonacci_search)
    >>> print(f"Resultado: x = {result}, f(x) = {rosenbrock(result)}")
    """
    terminar = False
    xk = x0
    k = 0

    def gradiente(f, x, deltaX=0.001):
        grad = []
        for i in range(len(x)):
            xp = x.copy()
            xn = x.copy()
            xp[i] = xp[i] + deltaX
            xn[i] = xn[i] - deltaX
            grad.append((f(xp) - f(xn)) / (2 * deltaX))
        return np.array(grad)
    
    def hessian_matrix(f, x, deltaX):
        fx = f(x)
        N = len(x)
        H = []
        for i in range(N):
            hi = []
            for j in range(N):
                if i == j:
                    xp = x.copy()
                    xn = x.copy()
                    xp[i] = xp[i] + deltaX
                    xn[i] = xn[i] - deltaX
                    hi.append((f(xp) - 2 * fx + f(xn)) / (deltaX ** 2))
                else:
                    xpp = x.copy()
                    xpn = x.copy()
                    xnp = x.copy()
                    xnn = x.copy()
                    xpp[i] = xpp[i] + deltaX
                    xpp[j] = xpp[j] + deltaX
                    xpn[i] = xpn[i] + deltaX
                    xpn[j] = xpn[j] - deltaX
                    xnp[i] = xnp[i] - deltaX
                    xnp[j] = xnp[j] + deltaX
                    xnn[i] = xnn[i] - deltaX
                    xnn[j] = xnn[j] - deltaX
                    hi.append((f(xpp) - f(xpn) - f(xnp) + f(xnn)) / (4 * deltaX ** 2))
            H.append(hi)
        return np.array(H)

    while not terminar:
        grad = np.array(gradiente(f, xk))
        hessian = hessian_matrix(f, xk, deltaX=0.001)
        hessian_inv = np.linalg.inv(hessian)

        if np.linalg.norm(grad) < epsilon1 or k >= maxiter:
            terminar = True
        else:
            def alpha_funcion(alpha):
                return f(xk - alpha * np.dot(hessian_inv, grad))

            alpha = metodo(alpha_funcion, e=epsilon2, a=0.0, b=1.0)
            x_k1 = xk - alpha * np.dot(hessian_inv, grad)

            if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1
    return xk