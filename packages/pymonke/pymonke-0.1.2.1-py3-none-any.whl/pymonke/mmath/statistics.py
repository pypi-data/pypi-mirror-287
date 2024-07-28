import numpy as np

from typing import Sequence, Callable


# TODO change the reduced chi square function and translate the docstring to english.
def reduced_chi_square(f: Callable[[Sequence[float], float], float], x: np.ndarray, y: np.ndarray, y_err: np.ndarray,
                       params: Sequence[float]) -> float:
    """Calculates the reduced chi-square of a function f(x) with respect to the specified data points.
    
    :param f: Mathematical function of form f(params, x)
    :param x: Array of data points along independent axis
    :param y: Array of data points along dependent axis
    :param y_err: Array of uncertainties along dependent axis
    :param params: Sequence of parameters that define function f(x)
    """

    try:
        iter(x)
        iter(y)
    except TypeError:
        print("__x and/ or y not an iterable")
        exit(-1)

    try:
        iter(y_err)
    except TypeError:
        y_err = [y_err] * len(x)

    x, y, y_err = np.array(x), np.array(y), np.array(y_err)

    chi_square = np.sum((y - f(params, x)) ** 2 / y_err ** 2)
    return chi_square / (len(x) - len(params))
