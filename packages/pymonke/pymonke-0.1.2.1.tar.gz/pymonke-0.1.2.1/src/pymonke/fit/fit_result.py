import pandas as pd
from mypy_extensions import VarArg
import numpy as np
from numpy.typing import NDArray
from uncertainties import ufloat  # type: ignore
from uncertainties.core import Variable, AffineScalarFunc  # type: ignore

from dataclasses import dataclass, field
from typing import List, Callable, TypeAlias, Iterable, Any, Optional

_scalar: TypeAlias = int | float
_array: TypeAlias = np.ndarray | pd.Series
_numerical: TypeAlias = _scalar | _array
_measurement: TypeAlias = Variable | AffineScalarFunc
_func_type: TypeAlias = Callable[[_numerical, VarArg(_scalar)], _numerical]


@dataclass(repr=True)
class FitResult:
    """Object that stores data of a fitted model"""
    function: _func_type = field(repr=False)
    """The Function that was used as a fitting model."""

    parameter_names: List[str]
    """The names of the fitted parameters"""
    # parameter_values: np.ndarray
    # parameter_sigmas: np.ndarray
    parameter_measurements: NDArray[_measurement]
    """The values of the fitted parameters with their corresponding standard deviations."""
    reduced_chi_squared: float | None = field(default=None)
    """The reduced chi-squared calculated from the fitted model"""

    # TODO implement residual variance
    residual_variance: float | None = field(default=None)
    """No description provided yet."""

    @property
    def parameter_values(self) -> np.ndarray:
        """The nominal values of the fitted parameters."""
        return np.array([i.nominal_value for i in self.parameter_measurements])

    @property
    def parameter_sigmas(self) -> np.ndarray:
        """The standard deviations of the fitted parameters."""
        return np.array([i.std_dev for i in self.parameter_measurements])

    def eval(self, x: _numerical) -> float | np.ndarray:
        """Evaluate the function given with the parameter values

        :param x: Argument of function. Can be a _scalar value or an _array."""
        result = self.function(x, *self.parameter_values)
        if isinstance(result, Iterable):
            return np.array(result)
        else:
            return float(result)

    def as_dict(self, with_goodness: bool = True) -> dict[str, Any | float]:
        """Convert the FitResult object into a dictionary.

        :param with_goodness: Whether to include the goodness values in the dictionary.
        """
        result_: dict = dict()
        for name, x in zip(self.parameter_names, self.parameter_measurements):
            result_[name] = x

        if with_goodness:
            result_["reduced_chi_squared"] = self.reduced_chi_squared

        return result_

    def __getitem__(self, item: str) -> Variable | AffineScalarFunc:
        index: int = -1
        for i, name in enumerate(self.parameter_names):
            if name == item:
                index = i
        if index == -1:
            text = f"parameter name {item} not found."
            raise KeyError(text)

        return self.parameter_measurements[index]  # type: ignore

    def _set_reduced_chi_squared(self, x: _array, y: _array, sigma: _array) -> float:
        chi_squared = ((self.eval(x) - y) ** 2 / sigma ** 2).sum()
        result: float = chi_squared / (len(x) - len(self.parameter_names))
        self.reduced_chi_squared = result
        return result


def result(function: _func_type, x: _array, y: _array, sy: _array, *,
           param_names: list[str], params: Iterable[float | _measurement],
           params_std_dev: Optional[_array] = None, sx: Optional[Iterable[float]] = None) -> FitResult:
    """Creates a FitResult object and calculates goodness of fit.

    :param function: The function that was fitted. Has The Form f(float, float...) -> float
    :param x: Array of data points. It is assumed to be
    an independent variable.
    :param y: Array of data points. Dependent Variable, uncertainty has to be provided, either as own variable
    sy, if y is an _array of dtype=float, or in y itself if the dtype is a Variable of the uncertainty package.
    :param sy: Array of uncertainty of y.
    :param sx: Array of uncertainty of x.
    :param param_names: List of parameter names.
    :param params: List of calculated parameter values. Dtype is either float or Variable | AffineScalarFunc
    of uncertainty package.
    :param params_std_dev: Standard deviation of the parameter values. Does not need to be given if params already
    provides uncertainty.

    :return: FitResult object
    """
    param_data: NDArray[_measurement]
    if __iterable_is_type(params, (Variable, AffineScalarFunc)):
        param_data = np.array(params)  # type: ignore
    elif __iterable_is_type(params, float):
        assert params_std_dev is not None
        param_data = np.array([ufloat(x, err) for x, err in zip(params, params_std_dev)])  # type: ignore
    else:
        raise ValueError("parameters arguments must be either an iterable of floats or of numbers with uncertainties.")

    fit_result = FitResult(function, param_names, param_data)
    fit_result._set_reduced_chi_squared(x, y, sy)

    return fit_result


def __iterable_is_type(iterable: Iterable[Any], t: type | tuple) -> bool:
    """@private"""
    for i in iterable:
        if not isinstance(i, t):
            return False

    return True
