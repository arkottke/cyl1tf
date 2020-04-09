"""Cython interface with C implementation."""
# cython: language_level=3

import cython
import numpy as np

cimport numpy as np


cdef extern from "l1tf.h":
    # Main routine for l1 trend filtering
    int l1tf(const int n, const double *y, const double scale, double *x);
    # Utility for computingn the maximum value of lambda
    double l1tf_lambdamax(const int n, double *y);

@cython.embedsignature(True)
def calc_max_scale(np.ndarray[double, ndim=1, mode='c']y):
    cdef int n = y.shape[0]
    return l1tf_lambdamax(n, <double *>y.data)

@cython.embedsignature(True)
def calc_fit(np.ndarray[double, ndim=1, mode='c']y, scale=None, rel_scale=None):
    cdef int n = y.shape[0]
    cdef np.ndarray[double, ndim=1, mode='c'] x = \
            np.empty(n, dtype=np.float64)

    if scale is None and rel_scale:
        max_scale = calc_max_scale(y)
        scale = rel_scale * max_scale
    elif scale and rel_scale is None:
        pass
    else:
        raise NotImplementedError

    l1tf(n, <double *>y.data, scale, <double *>x.data)
    return x
