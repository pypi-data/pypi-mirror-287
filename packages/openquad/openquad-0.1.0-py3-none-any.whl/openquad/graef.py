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
from .data.graef import (
    S2_GAUSS_METHODS,
    S2_SPHERICAL_DESIGNS,
    SO3_GAUSS_METHODS,
    SO3_CHEBYSHEV_METHODS,
)


class GraefS2Gauss(AtomicS2Quadrature, QuadratureWithDegree):

    _TABLE = np.asarray(S2_GAUSS_METHODS, dtype=int)
    _available_sizes = _TABLE[:, 1]
    _available_degrees = _TABLE[:, 0]

    def _points_weights(self):
        """FFT optimized Gauss-type S2 quadrature schemes from Manuel Gräf.

        Quadrature points and weights taken from:
        https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/

        Returns
        -------
        points : ndarray
            Sample points.
        weights : ndarray
            Quadrature weights.

        """
        points, weights = self._load_points_weights('graef', 's2_gauss')
        weights = weights * (4*np.pi)
        return points, weights


class GraefS2Design(AtomicS2Quadrature, QuadratureWithDegree):

    _TABLE = np.asarray(S2_SPHERICAL_DESIGNS, dtype=int)
    _available_sizes = _TABLE[:, 1]
    _available_degrees = _TABLE[:, 0]

    def _points_weights(self):
        """FFT optimized S2 spherical designs from Manuel Gräf.

        Quadrature points and weights taken from:
        https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/

        Returns
        -------
        points : ndarray
            Sample points.
        weights : ndarray
            Quadrature weights.

        """
        points, weights = self._load_points_weights('graef', 's2_design')
        weights = weights * (4*np.pi)
        return points, weights


class GraefSO3Gauss(AtomicSO3Quadrature, QuadratureWithDegree):

    _TABLE = np.asarray(SO3_GAUSS_METHODS, dtype=int)
    _available_sizes = _TABLE[:, 1]
    _available_degrees = _TABLE[:, 0]

    def _points_weights(self):
        """FFT optimized Gauss-type SO3 quadrature schemes from Manuel Gräf.

        Quadrature points and weights taken from:
        https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/

        Returns
        -------
        points : ndarray
            Sample points.
        weights : ndarray
            Quadrature weights.

        """
        points, weights = self._load_points_weights('graef', 'so3_gauss')
        weights = weights * (8*np.pi**2)
        return points, weights


class GraefSO3Chebyshev(AtomicSO3Quadrature, QuadratureWithDegree):

    _TABLE = np.asarray(SO3_CHEBYSHEV_METHODS, dtype=int)
    _available_sizes = _TABLE[:, 1]
    _available_degrees = _TABLE[:, 0]

    def _points_weights(self):
        """FFT optimized equal-weight SO3 quadrature schemes from Manuel Gräf.

        Quadrature points and weights taken from:
        https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/

        Returns
        -------
        points : ndarray
            Sample points.
        weights : ndarray
            Quadrature weights.

        """
        points, weights = self._load_points_weights('graef', 'so3_chebyshev')
        weights = weights * (8*np.pi**2)
        return points, weights
