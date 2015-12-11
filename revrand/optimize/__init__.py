"""
The :mod:`revrand.optimize` module provides a standardized interface to
popular optimization libraries and tools, such as NLopt and ``scipy.optimize``,
and also supports custom optimization methods.
"""

from .sgd import (sgd, sgd_u)
from .sgd_spark import (sgd_spark, sgd_u_spark)
from .sgd_updater import (AdaGrad, AdaDelta, Momentum)
from .base import (minimize,
                   minimize_bounded_start,
                   candidate_start_points_lattice,
                   candidate_start_points_random)

__all__ = [
    'sgd',
    'sgd_spark'
    'minimize',
    'minimize_bounded_start',
    'candidate_start_points_lattice',
    'candidate_start_points_random',
]
