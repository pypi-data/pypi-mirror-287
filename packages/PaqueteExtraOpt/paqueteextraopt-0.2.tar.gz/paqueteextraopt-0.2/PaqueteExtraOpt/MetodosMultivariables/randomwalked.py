import numpy as np

def caminata_aleatoria(f, x0, step, iter_max):
    """
    Este método intenta encontrar un mínimo local de la función `f` realizando 
    pasos aleatorios desde el punto inicial `x0`.

    :param f: La función objetivo que se va a minimizar.
    :type f: function
    :param x0: El punto inicial desde donde se empieza la caminata aleatoria.
    :type x0: numpy.ndarray
    :param step: La magnitud máxima del paso aleatorio.
    :type step: float
    :param iter_max: El número máximo de iteraciones a realizar.
    :type iter_max: int
    :return: El punto donde se encontró el mínimo local.
    :rtype: numpy.ndarray
    :raises ValueError: Si `x0` no es un numpy.ndarray.
    
    :Ejemplo:

    >>> import numpy as np
    >>> def f(x):
    >>>     return np.sum(x**2)
    >>> x0 = np.array([1.0, 1.0])
    >>> step = 0.1
    >>> iter_max = 1000
    >>> result = caminata_aleatoria(f, x0, step, iter_max)
    >>> print(result)
    """
    x = x0
    
    for i in range(iter_max):
        x_nuevo = x + np.random.uniform(-step, step, size=x.shape)
        if f(x_nuevo) < f(x):
            x = x_nuevo
    return x