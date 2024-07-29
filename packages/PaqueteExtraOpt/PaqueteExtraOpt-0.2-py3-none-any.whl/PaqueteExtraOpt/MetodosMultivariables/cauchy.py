import numpy as np

def cauchy(f, x0, epsilon1, epsilon2,  maxiter, metodo):
    
    """
    Este método intenta encontrar un mínimo local de la función `f` usando el gradiente descendente y una búsqueda de línea
    con el método especificado.

    :param f: La función objetivo que se va a minimizar.
    :type f: function
    :param x0: El punto inicial desde donde comienza la optimización.
    :type x0: numpy.ndarray
    :param epsilon1: El umbral para la norma del gradiente bajo el cual se considera que la solución ha convergido.
    :type epsilon1: float
    :param epsilon2: El umbral para la norma del cambio relativo en `xk` bajo el cual se considera que la solución ha convergido.
    :type epsilon2: float
    :param maxiter: El número máximo de iteraciones.
    :type maxiter: int
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
    >>> x0=np.array([0.0, 0.0])
    >>> epsilon1=0.001
    >>> epsilon2=0.001
    >>> max_iter=100
    >>> alpha=0.2
    >>> result = print(cauchy(f, x0, epsilon1, epsilon2, max_iter, fibonacci_search))
    >>> print(result)
    """
    def gradiente(f, x, deltaX=0.001):
        grad=[]
        for i in range(0, len(x)):
            xp=x.copy()
            xn=x.copy()
            xp[i]=xp[i]+deltaX
            xn[i]=xn[i]-deltaX
            grad.append((f(xp)-f(xn))/(2*deltaX))
        return grad
    
    terminar=False
    xk=x0
    k=0

    while not terminar:
        grad=np.array(gradiente(f, xk))

        if np.linalg.norm(grad)<epsilon1 or k>=maxiter:
            terminar=True
        else:
            def alpha_funcion(alpha):
                return f(xk-alpha*grad)
            
            alpha=metodo(alpha_funcion, e=epsilon2, a=0.0, b=1.0) 
            x_k1=xk-alpha*grad

            if np.linalg.norm(x_k1-xk)/(np.linalg.norm(xk)+0.00001) <= epsilon2:
                terminar=True
            else:
                k=k+1
                xk=x_k1
    return xk