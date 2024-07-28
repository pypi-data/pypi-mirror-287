# PyMonke

PyMonke is a python package with helpful tools for scientific reports and data analysis.

+ GitHub Page: https://github.com/GabrielRemi/pymonke
+ <a href="https://html-preview.github.io/?url=https://github.com/GabrielRemi/pymonke/blob/main/build/pymonke.html">
  Documentation
  </a>

## Installation

```commandline
pip install pymonke
```

---

## Using the GUI for fitting

The gui can be run either from the command line with

```commandline
python -m pymonke --run-gui
```

or inside your python script, e.g.

```python
import matplotlib.pyplot as plt
from pymonke import run_gui, Fit

fit: Fit = run_gui()
fit.plot()
plt.show()
```

The command `run_gui` runs the application and after quitting returns a `Fit` object with the result.
With the method `plot` the results can be plotted with matplotlib.

### Read Data

Below is a screenshot of the application. On the left is the data reading section. In the first line
the file with the data (only data with type .txt or .csv work for now) can be inserted and read.
If one already did a fit and saved the meta data into a .json file, this file can be open in the
Entry Widget below.<br>
In the Entry widgets marked with X and Y should be inserted the column names with the x and y array.
The uncertainties should be found automatically.<br>
To save the meta data, insert the save file in the Entry below.

### Plot and fit the data

In the middle is the plotting section. With `plotting arguments` additional arguments can be inserted
for changing the visuals of the plot. the arguments correspond to the same arguments of the matplotlib
`errorbar` function. <br>
On the bottom right the results of the fit can be saved in a file. The file should be of the .json type

### Creating a Fit

On the right section the fits can be created. First, a fit has to be added by replacing the "Add Fit"
inside the OptionBox by another fit name. After that, on the top a mathematical function can be
inserted and the parameter names will be extracted automatically. They can also be renamed in the entry below.
Because common function like the normal distribution are quite long expression, is it possible to insert
those function by their name, for example "gauss" for a normal distribution.
The Fitting method can be chosen in the right OptionBox. The Current options
are `OLS` for `scipy.optimize.curve_fit` and `ODR` for `scipy.odr.ODR`.
After settings the start parameters and the fitting limits, the fit can be executed.<br>
When defining labels for the plots, the values of the calculated parameters can be accessed by #param_name.
With `#param_name.value` or `#param_name.err` only the nominal value or the standard deviation can be accessed.


<img src="./misc/img.png">
