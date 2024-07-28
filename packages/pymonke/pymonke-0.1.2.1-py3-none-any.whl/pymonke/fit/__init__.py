"""Package to handle fitting with the scipy package. The Idea is to provide a faster way
to fit data in nore more than 3 lines of code.

Example
>>> from pymonke.fit import Fit, FitResult
>>>
>>> # define the meta data somewhere here, optionally also the fitting data
>>> # in a pandas DataFrame.
>>>
>>> fit = Fit(meta=meta, data=data)  # define fit object. If data is None,
>>> # define a file path for your data in the meta
>>> out: dict[str, FitResult] = fit.run()  # runs the fit for every fit
>>> # instruction defined in meta
>>> fit.plot()  # plots the fit with its data

To see which arguments the meta dictionary can take, generate the following dict:
>>> from pymonke.fit import generate_meta_dict
>>> meta = generate_meta_dict()
"""




from .fit import Fit
from .fit_result import FitResult
from .parse import RepetitionError
from .__misc import generate_meta_dict
