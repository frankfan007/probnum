"""
ProbNum
=====
Probabilistic Numerics in Python.
  1. Linear Algebra
  2. Quadrature
  3. Differential Equations
  4. Bayesian filtering and smoothing
and more.


Available subpackages and modules
---------------------------------
random_variables
    Random variables.
linalg
    Probabilistic numerical linear algebra.
quad
    Bayesian quadrature / numerical integration.
filtsmooth
    Bayesian filtering and smoothing.
diffeq
    Probabilistic solvers for ordinary differential equations.
"""
# -*- coding: utf-8 -*-
from pkg_resources import DistributionNotFound, get_distribution

from . import diffeq, filtsmooth, linalg, linops, quad, random_variables, utils
from .random_variables import RandomVariable, asrandvar

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound
