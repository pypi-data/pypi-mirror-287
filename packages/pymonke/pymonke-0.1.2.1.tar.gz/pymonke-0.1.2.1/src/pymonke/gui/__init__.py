"""Package for Pymonke's GUI for data fitting. To use this package,
either run

>>> python -m pymonke --run-gui

in the command line, or inside your python code:

>>> from pymonke import run_gui
>>> fit = run_gui()

run_gui() executes the applications and after quitting, retuns a Fit object.
"""

try:
    from icecream import ic, _install, argumentToString
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa
    """@private"""
    _install = lambda: None

from .misc import EntryError


_install()


