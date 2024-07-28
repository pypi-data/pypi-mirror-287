from typing import List, TypeAlias

import math
import numpy as np
from pandas import Series

_scalar: TypeAlias = float | int
_array: TypeAlias = np.ndarray | Series
_numeric: TypeAlias = _scalar | _array


def roundup(x: _numeric, r: int = 2) -> _numeric:
    """Always rounds the input value up to the specified decimal place. Input can be a number,
    but also a numpy Array or a pandas Series.

    :param x: The value / values to roundup
    :param r: Decimal place at which to round up the value(s)"""
    a: _numeric = x * 10 ** r
    a = np.ceil(a)
    a = a * 10 ** (-r)

    return np.around(a, r)




