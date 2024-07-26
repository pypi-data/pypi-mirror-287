# OpenQuad - open database for multi-dimensional numerical integration
# Copyright (C) 2024  Alexander Blech
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library. If not, see <https://www.gnu.org/licenses/>.

import numpy as np

from .base import (AtomicSO3Quadrature, AtomicS2Quadrature, QuadratureWithDegree)
from .data.womersley import S2_SPHERICAL_DESIGNS


class WomersleyS2Design(AtomicS2Quadrature, QuadratureWithDegree):

    _TABLE = np.asarray(S2_SPHERICAL_DESIGNS, dtype=int)
    _available_sizes = _TABLE[:, 1]
    _available_degrees = _TABLE[:, 0]

    def __init__(self, *args, symmetric=None, **kwargs):
        super().__init__(*args, symmetric=symmetric, **kwargs)

    def _points_weights(self, symmetric):
        """S2 spherical designs from Womersley.

        S2 spherical designs taken from:
        https://web.maths.unsw.edu.au/~rsw/Sphere/

        Returns
        -------
        points : ndarray
            Sample points.
        weights : ndarray
            Quadrature weights.

        """
        if symmetric is not None:
            if symmetric:
                suffix = '_sym'
            else:
                suffix = '_nosym'
            points, weights = self._load_points_weights(
                'womersley',
                's2_design',
                suffix,
            )
        if symmetric is None:
            # First try to find a symmetric method. If no present, try
            # asymmetric
            try:
                points, weights = self._load_points_weights(
                    'womersley',
                    's2_design',
                    '_sym',
                )
            except FileNotFoundError:
                points, weights = self._load_points_weights(
                    'womersley',
                    's2_design',
                    '_nosym',
                )
        weights = weights * (4*np.pi)
        return points, weights


class WomersleySO3Chebyshev(AtomicSO3Quadrature, QuadratureWithDegree):

    _TABLE = np.asarray(S2_SPHERICAL_DESIGNS, dtype=int)
    _available_sizes = _TABLE[:, 1] // 2
    _available_degrees = (_TABLE[:, 0] - 1) // 2
    # degree_SO3 corresponds to degree_S3 = 2*degree_SO3 + 1

    def _points_weights(self):
        """SO3 quadrature method based on S3 spherical designs from Womersley.

        S3 spherical designs taken from:
        https://web.maths.unsw.edu.au/~rsw/Sphere/

        Returns
        -------
        points : ndarray
            Sample points.
        weights : ndarray
            Quadrature weights.

        """
        msg = "SO3 quadratures from Womersley not yet implemented"
        raise NotImplementedError(msg)

        points, weights = self._load_points_weights('womersley', 's3_design')
        # data contains the cartesian coordinates
        # TODO: identify opposite points
        # TODO: convert to Euler angle representation
        # TODO: remove NotImplementedError at beginning of this method
        points = ...
        weights = np.ones(self.size) / self.size * (8*np.pi**2)
        return points, weights
