from matplotlib.axes import Axes

from .app import App
from pymonke.fit import FitResult, Fit

try:
    import scienceplots
except Exception:
    pass


def run() -> Fit:
    """Run the Fitting GUI and return a Fit object after quitting."""
    app = App()
    app.mainloop()
    if app.fit is None:
        raise Exception("No Fit found.")
    return app.fit

