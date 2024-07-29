
def newton_raphson(x_0, f, E):
    """
    Encuentra una raíz de una función unidimensional utilizando el método de Newton-Raphson.

    El método de Newton-Raphson es un método iterativo para encontrar soluciones de ecuaciones no lineales. En cada iteración, el método utiliza la derivada de la función para aproximar una mejor solución a la raíz de la ecuación.

    :param x_0: El valor inicial para el punto de partida del método iterativo.
    :type x_0: float
    :param f: La función objetivo.
    :type f: function
    :param E: La tolerancia para el criterio de convergencia, el proceso se detiene cuando \(|f'(x_{\text{next}})| < E\).
    :type E: float
    :return: El valor de \(x\) que aproxima una raíz de la función.
    :rtype: float

    :Ejemplo:

    >>> def funcion_objetivo(x):
    >>>     return x**3 - x - 2
    >>> raiz = newton_raphson(1.0, funcion_objetivo, 1e-5)
    >>> print(f"Raíz encontrada: x = {raiz}, f(x) = {funcion_objetivo(raiz)}")
    """
    def primera_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - f(x - delta)) / (2 * delta)

    def segunda_derivada(x, f):
        delta = 0.0001
        return (f(x + delta) - 2 * f(x) + f(x - delta)) / (delta ** 2)
    
    k = 1

    while True:
        f_primera = primera_derivada(x_0, f)
        f_segunda = segunda_derivada(x_0, f)
        x_next = x_0 - (f_primera / f_segunda)
        f_prima_next = primera_derivada(x_next, f)
        
        if abs(f_prima_next) < E:
            break
        
        k += 1
        x_0 = x_next

    return x_next