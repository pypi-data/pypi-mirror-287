import numpy as np 

def rastrigin(x):
        
    """
    La función Rastrigin es una función objetivo comúnmente utilizada en pruebas de algoritmos de optimización. Es una función no convexa con un mínimo global en el origen, y su diseño es adecuado para evaluar la capacidad de los algoritmos para explorar un espacio de búsqueda con múltiples óptimos locales.

    :param x: Un vector de números reales en el cual se evalúa la función Rastrigin.
    :type x: numpy.ndarray
    :return: El valor de la función Rastrigin evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.1, 0.2])
    >>> valor = rastrigin(x)
    >>> print(f"Valor de Rastrigin en x: {valor}")
  

    """
    A=10
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def ackley(x):
    
    """
    La función Ackley es una función objetivo utilizada en pruebas de algoritmos de optimización. Es una función no convexa con un mínimo global en el origen, y su diseño es adecuado para evaluar la capacidad de los algoritmos para explorar un espacio de búsqueda con múltiples óptimos locales.

    :param x: Un vector de números reales en el cual se evalúa la función Ackley.
    :type x: numpy.ndarray
    :return: El valor de la función Ackley evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.1, 0.2])
    >>> valor = ackley(x)
    >>> print(f"Valor de Ackley en x: {valor}")

    """
    a = 20
    b = 0.2
    c = 2 * np.pi
    suma1 = x[0]**2 + x[1]**2
    suma2 = np.cos(c * x[0]) + np.cos(c * x[1])
    term1 = -a * np.exp(-b * np.sqrt(0.5 * suma1))
    term2 = -np.exp(0.5 * suma2)
    resul = term1 + term2 + a + np.exp(1)
    return resul

def himmelblau(x):
    
    """
    La función Himmelblau es una función objetivo utilizada en pruebas de algoritmos de optimización. Es una función no convexa con múltiples mínimos locales, y su diseño es adecuado para evaluar la capacidad de los algoritmos para explorar un espacio de búsqueda complejo.

    :param x: Un vector de dos números reales en el cual se evalúa la función Himmelblau.
    :type x: numpy.ndarray
    :return: El valor de la función Himmelblau evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([3.0, 2.0])
    >>> valor = himmelblau(x)
    >>> print(f"Valor de Himmelblau en x: {valor}")

    """
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def sphere(x):
    
    """
    La función Sphere es una función objetivo utilizada en pruebas de algoritmos de optimización. Es una función convexa con un único mínimo global en el origen, y su diseño es adecuado para evaluar la capacidad de los algoritmos para converger a un mínimo global en un espacio de búsqueda suave.

    :param x: Un vector de números reales en el cual se evalúa la función Sphere.
    :type x: numpy.ndarray
    :return: El valor de la función Sphere evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> import numpy as np
    >>> x = np.array([1.0, 2.0, 3.0])
    >>> valor = sphere(x)
    >>> print(f"Valor de Sphere en x: {valor}")

    """
    return np.sum(np.square(x))

def rosenbrock(x):
    
    """
    También conocida como la función "valle de Rosenbrock", es una función no convexa con un mínimo global en el punto (1, 1, ..., 1). Su forma es útil para evaluar el rendimiento de los algoritmos en espacios de búsqueda multidimensionales.

    :param x: Un vector de números reales en el cual se evalúa la función de Rosenbrock.
    :type x: numpy.ndarray
    :return: El valor de la función de Rosenbrock evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([1.0, 1.0])
    >>> valor = rosenbrock(x)
    >>> print(f"Valor de Rosenbrock en x: {valor}")

    """
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def beale(x):
    
    """
    La función de Beale es una función objetivo utilizada en pruebas de algoritmos de optimización, especialmente en problemas de minimización. Es una función no convexa con un mínimo global en el punto (3, 0.5). La función es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en un espacio de búsqueda con características no lineales.

    :param x: Un vector de números reales en el cual se evalúa la función de Beale. El vector debe tener exactamente dos elementos.
    :type x: numpy.ndarray
    :return: El valor de la función de Beale evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([3.0, 0.5])
    >>> valor = beale(x)
    >>> print(f"Valor de Beale en x: {valor}")

    """
    return ((1.5 - x[0] + x[0] * x[1])**2 +
            (2.25 - x[0] + x[0] * x[1]**2)**2 +
            (2.625 - x[0] + x[0] * x[1]**3)**2)

def goldstein(self, x):
    
    """
    La función de Goldstein-Price es una función objetivo compleja utilizada en pruebas de algoritmos de optimización. Tiene múltiples óptimos locales y un único mínimo global en el punto (0, 0). Es útil para evaluar la capacidad de los algoritmos para manejar problemas no convexos con varios mínimos locales.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Goldstein-Price.
    :type x: numpy.ndarray
    :return: El valor de la función de Goldstein-Price evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = goldstein(x)
    >>> print(f"Valor de Goldstein-Price en x: {valor}")

    """
    a = (1 + (x[0] + x[1] + 1)**2 * 
                 (19 - 14 * x[0] + 3 * x[0]**2 - 14 * x[1] + 6 * x[0] * x[1] + 3 * x[1]**2))
    b = (30 + (2 * x[0] - 3 * x[1])**2 * 
                 (18 - 32 * x[0] + 12 * x[0]**2 + 48 * x[1] - 36 * x[0] * x[1] + 27 * x[1]**2))
    return a * b

def booth(x):
    
    """
    La función de Booth es una función objetivo utilizada en pruebas de algoritmos de optimización. Tiene un mínimo global en el punto (1, 3) y es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en problemas simples y no convexos.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Booth.
    :type x: numpy.ndarray
    :return: El valor de la función de Booth evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([1.0, 3.0])
    >>> valor = booth(x)
    >>> print(f"Valor de Booth en x: {valor}")

    """
    return (x[0] + 2 * x[1] - 7)**2 + (2 * x[0] + x[1] - 5)**2

def bunkin(x):
    """
    función Bunkin es no convexa con un mínimo global en el punto (0, -10). Esta función es útil para evaluar algoritmos en problemas de búsqueda con características no lineales.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Bunkin.
    :type x: numpy.ndarray
    :return: El valor de la función de Bunkin evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, -10.0])
    >>> valor = bunkin(x)
    >>> print(f"Valor de Bunkin en x: {valor}")

    """
    return 100 * np.sqrt(np.abs(x[1] - 0.001 * x[0]**2)) + 0.01 * np.abs(x[0] + 10)

def matyas(x):
    
    """
    La función de Matyas es una función objetivo utilizada en pruebas de algoritmos de optimización. Tiene un mínimo global en el punto (0, 0) y es útil para evaluar la capacidad de los algoritmos para encontrar mínimos en problemas con características suaves.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Matyas.
    :type x: numpy.ndarray
    :return: El valor de la función de Matyas evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = matyas(x)
    >>> print(f"Valor de Matyas en x: {valor}")

    """  
    return 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]

def levi(x):
    
    """
    La función de Levi tiene un mínimo global en el punto (1, 1) y es adecuada para evaluar la capacidad de los algoritmos para encontrar el mínimo en problemas no convexos.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Levi.
    :type x: numpy.ndarray
    :return: El valor de la función de Levi evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([1.0, 1.0])
    >>> valor = levi(x)
    >>> print(f"Valor de Levi en x: {valor}")
    >>> # Debería mostrar un valor cercano a 0.0, ya que (1.0, 1.0) es el mínimo global de la función de Levi.

    """
    a = np.sin(3 * np.pi * x[0])**2
    b= (x[0] - 1)**2 * (1 + np.sin(3 * np.pi * x[1])**2)
    c= (x[1] - 1)**2 * (1 + np.sin(2 * np.pi * x[1])**2)
    return a + b + c

def threehumpcamel(x):
    
    """
    La función Three-Hump Camel tiene un mínimo global en el punto (0, 0) y es útil para evaluar la capacidad de los algoritmos para manejar problemas con múltiples mínimos locales.

    :param x: Un vector de dos números reales en el cual se evalúa la función Three-Hump Camel.
    :type x: numpy.ndarray
    :return: El valor de la función Three-Hump Camel evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = threehumpcamel(x)
    >>> print(f"Valor de Three-Hump Camel en x: {valor}")
  
    """
    return 2 * x[0]**2 - 1.05 * x[0]**4 + (x[0]**6) / 6 + x[0] * x[1] + x[1]**2

def easom(x):
    
    """
    La función de Easom tiene un mínimo global en el punto (π, π) y es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en problemas con una estructura bien definida.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Easom.
    :type x: numpy.ndarray
    :return: El valor de la función de Easom evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([np.pi, np.pi])
    >>> valor = easom(x)
    >>> print(f"Valor de Easom en x: {valor}")

    """
    return -np.cos(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - np.pi)**2 - (x[1] - np.pi)**2)

def crossintray(x):
    
    """
    La función Cross-In-Tray es una función objetivo utilizada en pruebas de algoritmos de optimización. Tiene múltiples óptimos locales y un único mínimo global en el punto (0, 0). Es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en un espacio de búsqueda con características no lineales.

    :param x: Un vector de dos números reales en el cual se evalúa la función Cross-In-Tray.
    :type x: numpy.ndarray
    :return: El valor de la función Cross-In-Tray evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = crossintray(x)
    >>> print(f"Valor de Cross-In-Tray en x: {valor}")
    """
    op = np.abs(np.sin(x[0]) * np.sin(x[1]) * np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2) / np.pi)))
    return -0.0001 * (op + 1)**0.1

def eggholder(x):
    
    """
    La función de Eggholder tiene un mínimo global en el punto (-512, 404.2319) y es útil para evaluar la capacidad de los algoritmos para encontrar mínimos en espacios de búsqueda complejos.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Eggholder.
    :type x: numpy.ndarray
    :return: El valor de la función de Eggholder evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([-512.0, 404.2319])
    >>> valor = eggholder(x)
    >>> print(f"Valor de Eggholder en x: {valor}")
    """
    a = -(x[1] + 47) * np.sin(np.sqrt(np.abs(x[0] / 2 + (x[1] + 47))))
    b = -x[0] * np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))
    return a + b

def holdertable(x):
    """
    La función Holder Table  es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en un espacio de búsqueda con características complejas.

    :param x: Un vector de dos números reales en el cual se evalúa la función Holder Table.
    :type x: numpy.ndarray
    :return: El valor de la función Holder Table evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([8.05502, 9.66459])
    >>> valor = holdertable(x)
    >>> print(f"Valor de Holder Table en x: {valor}")
    """
    return -np.abs(  np.sin(x[0])*np.cos(x[1]) * np.exp(np.abs(1-((np.sqrt(x[0]**2 + x[1]**2))/(np.pi))))   )

def mccormick(x):
    """
    La función de McCormick es una función objetivo utilizada en pruebas de algoritmos de optimización. Tiene un mínimo global en el punto (-0.54719, -1.54719) y es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en problemas con características no convexas.

    :param x: Un vector de dos números reales en el cual se evalúa la función de McCormick.
    :type x: numpy.ndarray
    :return: El valor de la función de McCormick evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([-0.54719, -1.54719])
    >>> valor = mccormick(x)
    >>> print(f"Valor de McCormick en x: {valor}")
    """
    return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5 * x[0] + 2.5 * x[1] + 1

def schaffer2(x):
    
    """
    La función de Schaffer N.2 es una función objetivo utilizada en pruebas de algoritmos de optimización. Tiene un mínimo global en el punto (0, 0) y es útil para evaluar la capacidad de los algoritmos para manejar problemas con múltiples óptimos locales.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Schaffer N.2.
    :type x: numpy.ndarray
    :return: El valor de la función de Schaffer N.2 evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = schaffer2(x)
    >>> print(f"Valor de Schaffer N.2 en x: {valor}")
    """ 
    numerador = np.sin(x[0]**2 - x[1]**2)**2 - 0.5
    denominador = (1 + 0.001 * (x[0]**2 + x[1]**2))**2
    return 0.5 + numerador / denominador

def schaffer_n4(x):
    
    """

    La función de Schaffer N.4 es una función objetivo utilizada en pruebas de algoritmos de optimización. Tiene un mínimo global en el punto (0, 0) y es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en un espacio de búsqueda con múltiples óptimos locales.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Schaffer N.4.
    :type x: numpy.ndarray
    :return: El valor de la función de Schaffer N.4 evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = schaffer_n4(x)
    >>> print(f"Valor de Schaffer N.4 en x: {valor}")
    """
    
    term1 = np.cos(np.sin(np.abs(x[0]**2 - x[1]**2)))**2
    term2 = 1 + 0.001 * (x[0]**2 + x[1]**2)
    return 0.5 + (term1 - 0.5) / term2

def styblinskitang(x):
    
    """
    La función de Styblinski-Tang tiene un mínimo global en el punto (0, 0, ..., 0) y es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en problemas de alta dimensionalidad.

    :param x: Un vector de números reales en el cual se evalúa la función de Styblinski-Tang. El vector debe tener al menos dos elementos.
    :type x: numpy.ndarray
    :return: El valor de la función de Styblinski-Tang evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = styblinskitang(x)
    >>> print(f"Valor de Styblinski-Tang en x: {valor}")
    """
    return np.sum(x**4 - 16 * x**2 + 5 * x) / 2

def shekel(x):
    
    """
    La función de Shekel tiene varios mínimos locales y es útil para evaluar la capacidad de los algoritmos para encontrar el mínimo en un espacio de búsqueda complejo.

    :param x: Un vector de dos números reales en el cual se evalúa la función de Shekel.
    :type x: numpy.ndarray
    :return: El valor de la función de Shekel evaluada en el vector `x`.
    :rtype: float

    :Ejemplo:

    >>> x = np.array([0.0, 0.0])
    >>> valor = shekel(x)
    >>> print(f"Valor de Shekel en x: {valor}")
    """
    a = np.array([[4, 4, 4, 4],
                [1, 1, 1, 1]])
    c = np.array([0.1, 0.2, 0.2, 0.4])
    result = 0
    for i in range(len(c)):
        result += 1 / (c[i] + (x[0] - a[0, i])**2 + (x[1] - a[1, i])**2)
    return result