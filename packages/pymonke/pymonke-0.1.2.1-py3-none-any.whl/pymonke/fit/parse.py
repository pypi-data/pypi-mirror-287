from mypy_extensions import VarArg
import nltk  # type: ignore
import numpy as np
from pandas import Series

from typing import Callable, List, Tuple, TypeAlias, Iterable, Dict
from .fit_result import FitResult

_scalar: TypeAlias = float | int
_array: TypeAlias = Series | np.ndarray
_numerical: TypeAlias = _scalar | _array
_func_type: TypeAlias = Callable[[VarArg(str)], str]


class RepetitionError(Exception):
    """Error raised when trying to change parameter names in a mathematical formula that already exist."""
    def __init__(self) -> None:
        super().__init__("Trying to change name of a parameter, but name already exists.")


def __gauss(*args: str) -> str:
    return f"({args[0]} * exp((-(x - {args[1]}) ** 2) / (2 * {args[2]} ** 2)))"


def __linear(*args: str) -> str:
    return f"({args[0]} * x + {args[1]})"


__ALPH_OPERATORS = {
    'arccos': 'np.arccos',
    'arccosh': 'np.arccosh',
    'arcsin': 'np.arcsin',
    'arcsinh': 'np.arcsinh',
    'arctan': 'np.arctan',
    'arctanh': 'np.arctanh',
    'cos': 'np.cos',
    'cosh': 'np.cosh',
    'sqrt': 'np.sqrt',
    'e': 'np.e',
    'exp': 'np.exp',
    'log': 'np.log',
    'pi': 'np.pi',
    'sin': 'np.sin',
    'sinh': 'np.sinh',
    'tan': 'np.tan',
    'tanh': 'np.tanh',
}

__SYMBOL_OPERATORS = {
    '*': '*',
    '+': '+',
    '-': '-',
    '/': '/',
    '^': '**',
}

__FUNCS: Dict[str, Tuple[_func_type, List[str]]] = {
    "gauss": (__gauss, ["a", "x0", "sigma"]),
    "linear": (__linear, ["m", "b"]),
}


def __get_unique_name(name: str, params: List[str]) -> str:
    if name not in params:
        return name
    i = 1
    while (out := f"{name}{i}") in params:
        i += 1
        continue

    return out


def __is_param(token: str) -> bool:
    answer = (token not in __ALPH_OPERATORS and token not in __FUNCS and token.isalnum() and
              not token.isnumeric() and token != "x")
    if answer and token[0].isnumeric():
        raise ValueError("param names cannot start with a number")
    return answer


def rename_parameters(_formula: str, rename: Dict[str, str]) -> str:
    """Rename some parameters in the given formula string.

    :param _formula: Represents a mathematical formula.
    :param rename: Dictionary with the current parameter names as keys and the new names as values
    """
    # check for duplicates in rename dict
    if len(rename.values()) != len(set(rename.values())):
        raise RepetitionError

    tokens = nltk.tokenize.wordpunct_tokenize(_formula)
    params = _get_params(tokens)
    for index, token in enumerate(tokens):
        for key in rename.keys():
            if (new := rename[key]) == key:
                continue
            else:
                if new in params:
                    raise RepetitionError
            if not __is_param(new):
                raise ValueError("invalid parameter name")
            if key == token:
                tokens[index] = new

    return "".join(tokens)


def replace_funcs(_formula: str) -> str:
    """Replace common function names like 'gauss' and 'linear' with their mathematical expressions.

    :param _formula: Represents a mathematical formula.
    """
    if _formula == "":
        return _formula
    tokens = nltk.tokenize.wordpunct_tokenize(_formula)
    params: List[str] = []
    for token in tokens:
        if __is_param(token) and token not in params:
            params.append(token)

    for index, token in enumerate(tokens):
        if token in __FUNCS:
            b = [__get_unique_name(i, params) for i in __FUNCS[token][1]]
            tokens[index] = __FUNCS[token][0](*b)
            params.extend(b)

    return "".join(tokens)


def _get_params(tokens: List[str]) -> List[str]:
    params: List[str] = []
    for index, token in enumerate(tokens):
        if __is_param(token):
            params.append(token)
    return params


def parse_function(_formula: str) -> Tuple[Callable[[_numerical, VarArg(float | int)], _numerical], List[str]]:
    """Creates a python function out of a string that represents a mathematical formula.
    x is the variable and all the other arguments are passed as positional arguments to the
    generated callable with the form f(x: float, *params) -> float.

    :return: A callable python function and a list of all the arguments mentioned in _formula.
    """
    tokens = nltk.tokenize.wordpunct_tokenize(_formula)
    params: List[str] = []
    for index, token in enumerate(tokens):
        if token in __ALPH_OPERATORS:
            tokens[index] = __ALPH_OPERATORS[token]
        elif __is_param(token) and token not in params:
            params.append(token)

    def function(x: _numerical, *_params: _scalar) -> _numerical:
        if isinstance(x, Iterable):
            return np.array([function(i, *_params) for i in x])
        else:
            try:
                float(x)
            except TypeError:
                raise TypeError(r"Argument x must be a number or an iterable.")
        nonlocal tokens, params
        _tokens = tokens.copy()
        for i, tok in enumerate(_tokens):
            if tok in params:
                param_index = params.index(tok)
                _tokens[i] = str(_params[param_index])
            if tok == "x":
                _tokens[i] = str(x)
        string = " ".join(_tokens)
        for op in __SYMBOL_OPERATORS.keys():
            string = string.replace(op, __SYMBOL_OPERATORS[op])
        return eval(string)

    try:
        function(0, *([0] * len(params)))
    except SyntaxError as e:
        raise SyntaxError(e)
    except ArithmeticError:
        pass

    return function, params


def _parse_variable_str(label_str: str, result: FitResult, latex: bool = False) -> str:
    """Reads a string that has variable names marked with '#' and replaces them with their values
    from the FitResult object."""
    res_dict = result.as_dict(with_goodness=True)
    tokens = label_str.split()
    for index, tok in enumerate(tokens):
        if tok[0] != "#":
            continue
        tok = tok[1:]
        key_error = f"Parameter {tok} not found. Please check if your parameters are correct."
        value_error = f"Cannot access attribute of parameter {tok}. Only #paramter.val or #paramter.err are "
        f"allowed as inputs"
        if "." not in tok:
            if tok == "chi":
                tokens[index] = str(round(res_dict["reduced_chi_squared"], 2))
            else:
                try:
                    if latex:
                        tokens[index] = "{:L}".format(res_dict[tok])  # type: ignore
                    else:
                        tokens[index] = str(res_dict[tok])

                except KeyError:
                    raise KeyError(key_error)
        else:
            try:
                param, attr = tok.split(".")
            except:
                raise ValueError(value_error)
            try:
                if attr == "val":
                    tokens[index] = str(res_dict[param].nominal_value)  # type: ignore
                elif attr == "err":
                    tokens[index] = str(res_dict[param].std_dev)  # type: ignore
                else:
                    raise ValueError(value_error)
            except KeyError:
                raise KeyError(key_error)

    return " ".join(tokens)
