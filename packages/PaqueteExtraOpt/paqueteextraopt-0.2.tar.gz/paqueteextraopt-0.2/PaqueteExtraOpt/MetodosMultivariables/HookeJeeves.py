import numpy as np 

def hooke_jeeves(f, x_initial, delta, alpha, epsilon):
    
    """
    Este método intenta encontrar un mínimo local de la función `f` utilizando un algoritmo de búsqueda directa.

    :param f: La función objetivo que se va a minimizar.
    :type f: function
    :param x_initial: El punto inicial desde donde comienza la optimización.
    :type x_initial: list or numpy.ndarray
    :param delta: El tamaño del paso para la búsqueda exploratoria.
    :type delta: list or numpy.ndarray
    :param alpha: El factor de reducción para el tamaño del paso.
    :type alpha: float
    :param epsilon: El umbral para determinar la convergencia.
    :type epsilon: float
    :return: El punto donde se encontró el mínimo local.
    :rtype: numpy.ndarray
    :raises ValueError: Si `x_initial` o `delta` no son listas o numpy.ndarrays.
    
    :Ejemplo:

    >>> import numpy as np
    >>> def himmelblau(x):
    >>>     return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2
    >>> x_initial = [-5, -2.5]
    >>> delta = [0.5, 0.25]
    >>> alpha = 2
    >>> epsilon = 0.1
    >>> result = hooke_jeeves(himmelblau, x_initial, delta, alpha, epsilon)
    >>> print(result)
    """
    def movimiento_exploratorio(xc, delta, func):
        x = np.copy(xc)
        for i in range(len(x)):
            f = func(x)
            x[i] += delta[i]
            f_mas = func(x)
            if f_mas < f:
                f = f_mas
            else:
                x[i] -= 2*delta[i]
                f_menos = func(x)
                if f_menos < f:
                    f = f_menos
                else:
                    x[i] += delta[i]
        return x
    
    x = np.array(x_initial)
    delta = np.array(delta)
    while True:
        x_nuevo = movimiento_exploratorio(x, delta, f)
        
        if np.array_equal(x, x_nuevo):
            if np.linalg.norm(delta) < epsilon:
                break
            else:
                delta /= alpha
                continue
        
        x_p = x_nuevo + (x_nuevo - x)
        x_p_nuevo = movimiento_exploratorio(x_p, delta, f)
        
        if f(x_p_nuevo) < f(x_nuevo):
            x = x_p_nuevo
        else:
            x = x_nuevo
    
    return x