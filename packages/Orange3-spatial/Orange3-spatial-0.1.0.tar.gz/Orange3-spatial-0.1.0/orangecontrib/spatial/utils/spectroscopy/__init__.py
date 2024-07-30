import numpy as np




def values_to_linspace(vals):
    """Find a near matching linspace for the values given.
    The problem is that some values can be missing and
    that they are inexact. The minumum and maximum values
    are kept as limits."""
    vals = np.asarray(vals[~np.isnan(vals)])
    if len(vals):
        vals = np.unique(vals)  # returns sorted array
        if len(vals) == 1:
            return vals[0], vals[0], 1
        minabsdiff = (vals[-1] - vals[0])/(len(vals)*100)
        diffs = np.diff(vals)
        diffs = diffs[diffs > minabsdiff]
        first_valid = diffs[0]
        # allow for a percent mismatch
        diffs = diffs[diffs < first_valid*1.01]
        step = np.mean(diffs)
        size = int(round((vals[-1]-vals[0])/step) + 1)
        return vals[0], vals[-1], size
    return None


def location_values(vals, linspace):
    vals = np.asarray(vals)
    if linspace is None or linspace[2] == 1:  # everything is the same value
        width = 1
    else:
        width = (linspace[1] - linspace[0]) / (linspace[2] - 1)
    start = 0
    if linspace is not None:
        start = linspace[0]
    return (vals - start) / width


def index_values(vals, linspace):
    """ Remap values into index of array defined by linspace. """
    return index_values_nan(vals, linspace)[0]


def index_values_nan(vals, linspace):
    """ Remap values into index of array defined by linspace.
    Returns two arrays: first contains the indices, the second invalid values."""
    positions = location_values(vals, linspace)
    return np.round(positions).astype(int), np.isnan(positions)
