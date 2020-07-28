import numpy as np


class _RandomVariableList(list):
    """List of RandomVariables with convenient access to means, covariances, etc."""

    def mean(self):
        return np.stack([rv.mean() for rv in self])

    def cov(self):
        return np.stack([rv.cov() for rv in self])

    def var(self):
        return np.stack([rv.distribution.var() for rv in self])

    def std(self):
        return np.stack([rv.distribution.std() for rv in self])

    def __getitem__(self, idx):
        """Make sure to wrap the result into a _RandomVariableList if necessary"""
        result = super().__getitem__(idx)
        if isinstance(result, list):
            result = _RandomVariableList(result)
        return result
